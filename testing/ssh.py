import paramiko
import string
import os

host = "pluton.kt.agh.edu.pl"
port = 22
username = "msztaba"
# needs to be hashed 
password = "############"

command = "ls"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

stdin, stdout, stderr = ssh.exec_command(command)
lines = stdout.readlines()
print(lines)