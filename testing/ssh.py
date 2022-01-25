import paramiko
import string
import os

host = "pluton.kt.agh.edu.pl"
port = 22
username = "msztaba"
# needs to be hashed
password = "##########"

# creating list of commands to be executed
try:
    with open("commands.txt", 'r') as my_file:
        content = my_file.read()
        content_list = content.split("\n")

    # creating connection
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, password)

    # executing commands
    for command in content_list:
        stdin, stdout, stderr = ssh.exec_command(command)
        lines = stdout.readlines()
        print(lines)
except:
    print("something went wrong")