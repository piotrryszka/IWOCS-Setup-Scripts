# SSH CONNECTION

# imports
from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException
from time import sleep
from datetime import datetime

from lib.data import password, username, decorator_1, server_ip

# establishing SSH connection
def ssh_con(file, host):
    # creating time stamp
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y")

    # configuration of network device
    cisco1 = {
        "device_type": f"cisco_ios",
        "host": f"{host}",
        "username": f"{username}",
        "password": f'{password}',
        # TODO: UNCOMMENT IT (change way of saving data)
        # session logger
        "session_log": f"device-logs/{file}---{host}.txt"
    }

    try:
        with ConnectHandler(**cisco1) as net_connect:
            # TFTP configuration download command
            our_command = f'copy tftp://{server_ip}/{file} startup-config'

            # ONE COMMAND WITH TFTP COPY
            net_connect.send_command_timing(our_command, cmd_verify=False)

            # waiting for tftp downloaded
            sleep(2)

            # sending confirmation of tftp copy
            net_connect.send_command_timing('\n', cmd_verify=False)

            # TODO: think about moving it to the next function
            # command for reloading
            net_connect.send_command_timing('reload', cmd_verify=False)

            # sending confirmation of reloading copy
            net_connect.send_command_timing('\n', cmd_verify=False)

            # waiting to give time to device react
            sleep(2)

    # error handling while ssh connection
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)
        print(decorator_1)

