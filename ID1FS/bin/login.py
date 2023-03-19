from cryptography.fernet import Fernet
import getpass


# PASSWORD
def write_key():
    key = Fernet.generate_key()
    with open("etc/ID1FS_key.key", "wb") as key_file:
        key_file.write(key)
def load_key():
    file = open("etc/ID1FS_key.key", "rb")
    key = file.read()
    file.close()
    return key
def add():
    user = input("Account name: ")
    passw = input("The password: ")
    with open('.etc/passwords.txt', 'a') as f:  # insted of open. colse.
        f.write(user + "| " + fer.encrypt(passw.encode()).decode() + "\n")
def view():
    passwords = {}
    with open('etc/passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()  # rstrip to not read \n
            user_, passw_ = data.split("|")  # "1|2|3" ==> ["1","2","3"]
            passwords[user_] = fer.decrypt(passw_.encode()).decode()
    return passwords
def login():
    psswrd = getpass.getpass("Enter your password: ")
    if view()["root"] == psswrd:
        return True
    return False
def change():
    passw = getpass.getpass("Your new password: ")
    passw2 = getpass.getpass("Retype your new password: ")
    if passw2 == passw:
        with open('etc/passwords.txt', 'w') as f:  # insted of open. colse.
            f.write("root| " + fer.encrypt(passw.encode()).decode() + "\n")
        return True
    else:
        print("Wrong password")
        return False



key = load_key()  # + master_passw.encode()
fer = Fernet(key)


