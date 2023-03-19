import rpyc
import sys
import logging
import base64
import login as lg

import subprocess


# logging and logger settings:
mylogs = logging.getLogger()
mylogs.setLevel(level=logging.DEBUG)

file = logging.FileHandler("log/ID1FS_client.log")
mylogs.addHandler(file)
file.setLevel(level=logging.WARNING)
fileformat = logging.Formatter("%(asctime)s:%(name)s:%(levelname)s:%(message)s")
file.setFormatter(fileformat)

consolehandler = logging.StreamHandler(stream=sys.stdout)
consolehandler.setLevel(logging.DEBUG)
streamformat = logging.Formatter("%(levelname)s:%(message)s")
consolehandler.setFormatter(streamformat)
mylogs.addHandler(consolehandler)


# ID1FS commands
def get(father, file):
    file_table = father.read(file)
    if not file_table:
        logging.info("File not found!")
        return

    for room in file_table:
        for host, port in room['room_adrs']:
            try:
                con = rpyc.connect(host, port=port).root
                data = con.get(room['room_id'])
                if data:
                    fh = open('data/' + file, 'ab')
                    fh.write(base64.b64decode(data))
                    fh.close()
                    break
            except Exception as e:
                continue
        else:
            logging.error("No rooms found. Possibly a corrupt file")


def put(father, source, dest):
    with open(source, 'rb') as imagefile:
        byteform = base64.b64encode(imagefile.read())
    dest_b = byteform
    size = len(dest_b)
    rooms = father.write(dest, size)
    DATA_splited = [dest_b[i:i + father.room_size] for i in range(0, len(dest_b), father.room_size)]
    i = 0
    for room in rooms:
        data = DATA_splited[i]
        i = i + 1
        room_id = room['room_id']
        children = room['room_adrs']

        child = children[0]
        children = children[1:]
        host, port = child

        con = rpyc.connect(host, port=port)
        con.root.put(room_id, data, children)


def help():
    logging.debug("ID1FS help!")
    print("help   : Listing all possible commands in ID1FS >>> help")
    print("put    : Upload a file from local to ID1FS >>> put [source file path][destination name]")
    print("get    : Export a file from ID1FS to local >>> get [destination name]")
    print("remove : Delete a file from ID1FS >>> remove  [destination name]")
    print("list   : List all existing files >>> list ")
    print("open   : Open a file >>> open [destination name]")
    print("status : Check current status (Up/Down) >>> status")
    print("chpass : Change your password >>> chpass")


def openn(file):
    try:
        subprocess.call(["open", 'data/' + file])
    except Exception as e:
        logging.error(e)


def removee(father, file):
    file_table = father.read(file)
    if not file_table:
        logging.error("File not found!")
        return
    try:
        for room in file_table:
            for host, port in room['room_adrs']:
                try:
                    con = rpyc.connect(host, port=port).root
                    con.remove(room['room_id'])
                except Exception as e:
                    continue
    except KeyError:
        logging.error("File not found!")

    try:
        father.removee(file)
    except:
        logging.error("An error occured, file not found!")


def listt(father):
    all_files = father.liste()
    if len(all_files) == 0:
        print("There is no files imported")
    else:
        print('Existing files:')
        for i in all_files:
            print(i)


def main(args):
    try:
        con = rpyc.connect("localhost", port=2131)
        father = con.root

        if args[0] == "get":
            if lg.login():
                try:
                    get(father, args[1])
                    logging.debug("File has been imported successfully")
                except KeyError:
                    logging.error("File doesnt exists!")
            else:
                logging.error("Wrong password!")
        elif args[0] == "put":
            if lg.login():
                try:
                    put(father, args[1], args[2])
                    logging.debug("File has been exported successfully")
                except IndexError:
                    logging.error("Syntax error of command put, try help!")
                except FileNotFoundError as e:
                    logging.error(e)
            else:
                logging.error("Wrong password!")
        elif args[0] == "help":
            help()
        elif args[0] == "open":
            openn(args[1])
        elif args[0] == "remove":
            if lg.login():
                try:
                    removee(father, args[1])
                    logging.debug("File has been removed successfully")
                except KeyError:
                    logging.error("File not found!")
            else:
                logging.error("Wrong password")
        elif args[0] == "list":
            listt(father)
        elif args[0] == "status":
            logging.debug("Server is UP!")
        elif args[0] == "chpass":
            if lg.login():
                if lg.change():
                    logging.debug("Password has been changed successfully")
            else:
                logging.error("Wrong password!")
        else:
            logging.error("Command not found! Try help")
    except ConnectionRefusedError:
        logging.error("An error occurred. Server is Down!")


if __name__ == "__main__":
    main(sys.argv[1:])


