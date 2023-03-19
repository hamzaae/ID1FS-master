'''
from configparser import ConfigParser

config = ConfigParser()

config["DEFAULT"] = {
    #fatherMaster:
    "ROOM_SIZE": 100,
    "REPLICATION_FACTOR": 2,
    "CHILD": {"1": ("127.0.0.1", 8000), "2": ("127.0.0.1", 9000),},
    #child:
    "DATA_DIR" = "/tmp/child/",
    "PORT" = 8888,
}

with open("bin/ID1FSconfig.conf", "w") as f:
    config.write(f)
'''