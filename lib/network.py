# SSH CONNECTION

# imports
from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException
from lib.data import password, username, decorator_1, server_ip
from time import sleep
from datetime import datetime

# establishing SSH connection
def ssh_con(file, host):
    # creating time stamp
    exact_time = datetime.date(datetime.now())
    cisco1 = {
        "device_type": f"cisco_ios",
#         "device_type": f"autodetect",
        "host": f"{host}",
        "username": f"{username}",
        "password": f'{password}',
#         "fast_cli": False,
        # logger
        "session_log": f"device-logs/{host}---{exact_time}.txt",
    }

    try:
        with ConnectHandler(**cisco1) as net_connect:

            # commands to be sent
            our_command = f'copy tftp://{server_ip}/{file} startup-config'
            print(our_command)

            # TODO: ONE COMMAND WITH TFTP COPY
            output = net_connect.send_command_timing(our_command, cmd_verify=False)
            sleep(2)

            # printing for tests
            output = net_connect.send_command_timing('\n', cmd_verify=False)
            print(output)

            # printing for tests
            output = net_connect.send_command_timing('reload', cmd_verify=False)
            print(output)

    # error handling while ssh connection
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)
        print(decorator_1)