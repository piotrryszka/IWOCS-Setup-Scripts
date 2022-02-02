# SSH CONNECTION

# imports
# NETMIKO
from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException
from lib.data import password, username, decorator_1

# TODO: ADD encryption and decryption also, adding threads to do some configuration faster for example 3 devices at once
# TODO: old keys in ssh connection, try to be able to connect to any device

# establishing SSH connection
def ssh_con(file, host):
    cisco1 = {
        # autodetect is very useful in network devices
        "device_type": f"autodetect",
        "host": f"{host}",
        "username": f"{username}",
        "password": f'{password}',
    }

    # creating list with commands from file
    with open(f"tftp-conf-files/{file}", 'r') as my_file:
            content = my_file.read()
            commands_list = content.split("\n")

    # executing commands for network device
    try:
        with ConnectHandler(**cisco1) as net_connect:
            for command in commands_list:
                # sending command
                output = net_connect.send_command(command)
                # printing output of command with error handling too
                print(output)
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)
        print(decorator_1)