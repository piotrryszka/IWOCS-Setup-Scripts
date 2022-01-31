# imports
# PARAMIKO
import paramiko
from lib.data import decorator_1, username, password

# NETMIKO
from netmiko import ConnectHandler
# this import is not important right now
from getpass import getpass

# need to add more arguments, like to make host, username, password correct in every case
def ip_connect(lang_dict, ip_number, file):
    # checking private configuration, needs to be deleted
    host = "pluton.kt.agh.edu.pl"

    # port is always the same
    port = 22

    # need to take ip_number from data or from main.py -> TODO: to check
    # host = f'172.30.100.{ip_number}'

    # creating list of commands to be executed, file to be chosen as arguments
    try:
        with open(f"tftp-conf-files/{file}", 'r') as my_file:
            content = my_file.read()
            content_list = content.split("\n")

        # creating connection
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, username, password)

        print(lang_dict['ssh_established'])
        print(decorator_1)

        # executing commands from file
        for command in content_list:
            stdin, stdout, stderr = ssh.exec_command(command)
            lines = stdout.readlines()
            print(lines)

        # closing connection
        ssh.close()
    except:
        print(lang_dict['ssh_failed'])
        print(decorator_1)

# CONF TO TRY_NETMIKO
host = "pluton.kt.agh.edu.pl"

# check if logs are possible to read after working on network device,

#TODO: ADD EXCPETIONS LIKE Netmikotimeoutexception, ssh exception etc
# TODO: ADD encryption and decryption also, adding threads to do some configuration faster for example 3 devices at once

# TODO: old keys in ssh connection, try to be able to connect to any device




def try_netmiko():
    cisco1 = {
        # autodetect is very useful in network devices
        "device_type": f"autodetect",
        "host": f"{host}",
        "username": f"{username}",
        "password": f'{password}',
    }

    # Show command that we execute.
    commands_list = ['ls', 'pwd', 'mkdir tescik', 'ls' ,'rmdir tescik']

    # executing commands for network device
    with ConnectHandler(**cisco1) as net_connect:
        for command in commands_list:
            # sending command
            output = net_connect.send_command(command)
            # printing output of command with error handling too
            print(output)
