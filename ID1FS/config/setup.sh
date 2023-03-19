#!/bin/bash 

sudo apt update
sudo apt install python3
sudo pip install rpyc
sudo pip install cryptography
alias ID1FS='python3 bin/client.py'
echo "setup DONE"
