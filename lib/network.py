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

    # configuration of network device
    cisco1 = {
        "device_type": f"cisco_ios",
        "host": f"{host}",
        "username": f"{username}",
        "password": f'{password}',
        # session logger
        "session_log": f"device-logs/ip: {host}|---|date: {exact_time}.txt",
    }

    try:
        with ConnectHandler(**cisco1) as net_connect:

            # TFTP configuration download command
            our_command = f'copy tftp://{server_ip}/{file} startup-config'

            # ONE COMMAND WITH TFTP COPY
            net_connect.send_command_timing(our_command, cmd_verify=False)

            # TODO: check in LAB if it is needed to wait here
            # waiting for tftp downloaded
            sleep(2)

            # sending confirmation of tftp copy
            net_connect.send_command_timing('\n', cmd_verify=False)

            # command for reloading
            net_connect.send_command_timing('reload', cmd_verify=False)

            # sending confirmation of reloading copy
            net_connect.send_command_timing('\n', cmd_verify=False)

    # error handling while ssh connection
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)
        print(decorator_1)