import rpyc
import uuid
import math
import random
import logging
import sys

from rpyc.utils.server import ThreadedServer
from configparser import ConfigParser

# logging and logger settings:
mylogs = logging.getLogger()
mylogs.setLevel(level=logging.INFO)

file = logging.FileHandler("log/ID1FS_fatherMaster.log")
mylogs.addHandler(file)
file.setLevel(level=logging.WARNING)
fileformat = logging.Formatter("%(asctime)s:%(name)s:%(levelname)s:%(message)s")
file.setFormatter(fileformat)

consolehandler = logging.StreamHandler(stream=sys.stdout)
consolehandler.setLevel(logging.INFO)
streamformat = logging.Formatter("%(levelname)s:%(message)s")
consolehandler.setFormatter(streamformat)
mylogs.addHandler(consolehandler)


class FatherMasterService(rpyc.Service):
    """
    file_room = {'file.txt': ["room1", "room2"]}
    room_child = {"room1": [1,3]}
    children = {"1": (127.0.0.1, 8000), "3": (127.0.0.1, 9000)}
    """
    # importing variables using config file
    config = ConfigParser()
    config.read("config/ID1FSconfig.conf")
    client = "DEFAULT"
    config_data = config[client]
    # declaring variables using config file
    file_room = {}
    room_child = {}
    room_size = int(config_data['ROOM_SIZE'])
    replication_factor = int(config_data['REPLICATION_FACTOR'])
    children = config_data['CHILDREN']


    def exposed_read(self, file):

        all_files = self.file_room.keys()
        mapping = []
        # iterate over all of file's blocks
        for rc in self.file_room[file]:
            child_adrs = []
            # get all children that contain that room
            for c_id in self.room_child[rc]:
                child_adrs.append(eval(self.children)[c_id])

            mapping.append({"room_id": rc, "room_adrs": child_adrs})
        return mapping

    def exposed_write(self, file, size):

        self.file_room[file] = []

        num_rooms = int(math.ceil(float(size) / self.room_size))
        return self.alloc_rooms(file, num_rooms)

    def exposed_liste(self):
        return self.file_room.keys()

    def exposed_removee(self, file):
        del self.file_room[file]

    def alloc_rooms(self, file, num_rooms):
        return_rooms = []
        for i in range(0, num_rooms):
            # generate a room
            room_id = str(uuid.uuid1())
            # allocate REPLICATION_FACTOR number of children
            child_ids = random.sample(list(eval(self.children).keys()), self.replication_factor)
            child_adrs = [eval(self.children)[m] for m in child_ids]
            self.room_child[room_id] = child_ids
            self.file_room[file].append(room_id)

            return_rooms.append(
                {"room_id": room_id, "room_adrs": child_adrs})
        return return_rooms



if __name__ == "__main__":
    t = ThreadedServer(FatherMasterService(), port=2131, protocol_config={
    'allow_public_attrs': True, })

    t.start()
