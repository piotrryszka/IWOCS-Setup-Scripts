# SSH CONNECTION

# imports
from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException
from lib.data import password, username, decorator_1
from time import sleep
from datetime import datetime

# establishing SSH connection
def ssh_con(file, host):
    # creating time stamp
    exact_time = datetime.date(datetime.now())
    cisco1 = {
        #"device_type": f"cisco_ios",
        "device_type": f"autodetect",
        "host": f"{host}",
        "username": f"{username}",
        "password": f'{password}',
        # logger
        "session_log": f"../device-logs/{host}---{exact_time}.txt",
    }

    server_ip = '172.30.100.91'


    # creating list with commands from file
#     with open(f"../tftp-conf-files/{file}") as my_file:
#             content = my_file.read()
#             commands_list = content.split("\n")
#
#     print(commands_list)

    # executing commands for network device
    try:
        with ConnectHandler(**cisco1) as net_connect:

            # TODO: ONE COMMAND WITH TFTP COPY
            output = net_connect.send_command(f'copy tftp://{server_ip}/{file} start', cmd_verify=False)
            # printing output of command with error handling too
            print(output)

#             for com in commands_list:
#                 # sending command
#                 output = net_connect.send_command(com, cmd_verify=False)
#                 # printing output of command with error handling too
#                 print(output)
    # error handling while ssh connection
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)
        print(decorator_1)