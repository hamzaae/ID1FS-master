import rpyc
import os
import sys
import logging
import subprocess


from configparser import ConfigParser
from rpyc.utils.server import ThreadedServer


# logging and logger settings:
mylogs = logging.getLogger()
mylogs.setLevel(level=logging.DEBUG)

file = logging.FileHandler("log/ID1FS_child.log")
mylogs.addHandler(file)
file.setLevel(level=logging.WARNING)
fileformat = logging.Formatter("%(asctime)s:%(name)s:%(levelname)s:%(message)s")
file.setFormatter(fileformat)

consolehandler = logging.StreamHandler(stream=sys.stdout)
consolehandler.setLevel(logging.DEBUG)
streamformat = logging.Formatter("%(levelname)s:%(message)s")
consolehandler.setFormatter(streamformat)
mylogs.addHandler(consolehandler)

# importing variables using config file
config = ConfigParser()
config.read("config/ID1FSconfig.conf")
client = "DEFAULT"
config_data = config[client]
# declaring variables using config file
PORT = int(config_data['PORT'])
DATA_DIR = config_data['DATA_DIR']


class Child(rpyc.Service):

    def exposed_put(self, room_id, data, children):
        logging.debug("Put room: " + room_id)
        out_path = os.path.join(DATA_DIR_c, room_id)
        with open(out_path, 'wb') as f:
            f.write(data)
        if len(children) > 0:
            self.forward(room_id, data, children)

    def exposed_get(self, room_id):
        logging.debug("Getting room: " + room_id)
        room_adrs = os.path.join(DATA_DIR_c, room_id)
        if not os.path.isfile(room_adrs):
            logging.debug("Room not found!")
            return None
        with open(room_adrs, 'rb') as f:
            return f.read()

    def exposed_remove(self, room_id):
        logging.debug("Deleting room: " + room_id)
        room_adrs = os.path.join(DATA_DIR_c, room_id)
        if not os.path.isfile(room_adrs):
            logging.error("Room not found!")
            return None
        else:
            subprocess.call(["rm", room_adrs])

    def forward(self, room_id, data, children):
        logging.debug("Forwarding room: " + room_id + str(children))
        next_child = children[0]
        children = children[1:]
        host, port = next_child

        rpyc.connect(host, port=port).root.put(room_id, data, children)


if __name__ == "__main__":
    PORT = int(sys.argv[1])
    DATA_DIR_c = sys.argv[2]

    if not os.path.isdir(DATA_DIR_c):
        os.mkdir(DATA_DIR_c)

    logging.debug("Starting child")
    t = ThreadedServer(Child(), port=PORT, logger=mylogs, protocol_config=
    {'allow_public_attrs': True, })
    try:
        t.start()
    except Exception as e:
        logging.error(e)
