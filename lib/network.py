# SSH CONNECTIONS

# imports
from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException
from time import sleep
from datetime import datetime

from config.data import password, username, decorator_1, server_ip, commands_list

# establishing SSH connection and downloading project configs
def ssh_con(file, host):
    # creating time stamp
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y")
    dateTimeObj = datetime.now()
    dateObj = dateTimeObj.date()
    dateStr = dateObj.strftime("%d.%m.%Y")
    # configuration of network device
    cisco1 = {
        "device_type": f"cisco_ios",
        "host": f"{host}",
        "username": f"{username}",
        "password": f'{password}',
        # session logger
        "session_log": f"logs/device_logs/{file}_{host}_{dateStr}.txt"
    }
    with ConnectHandler(**cisco1) as net_connect:
        try:
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

# sending commands to download input from devices
def ssh_download(host, device, command):
    # creating time stamp
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y")
    dateTimeObj = datetime.now()
    dateObj = dateTimeObj.date()
    dateStr = dateObj.strftime("%d.%m.%Y")
    # configuration of network device
    cisco1 = {
        "device_type": f"cisco_ios",
        "host": f"{host}",
        "username": f"{username}",
        "password": f'{password}',
        # session logger
        "session_log": f"logs/project_logs/{device}_{host}_{dateStr}.txt"
    }
    with ConnectHandler(**cisco1) as net_connect:
        try:
            # assigning command to sending command
            our_command = command

            # sending 'enter' to clear CLI window
            net_connect.send_command('\n', cmd_verify=False)

            # command sent to network device
            command_output = net_connect.send_command(our_command, cmd_verify=False)

            # replacing spaces in command with - char
            command = command.replace(' ', '-')

            # opening file and saving an output to the file
            with open(f'support/show-tech/{device}___{command}___{dateStr}.txt', 'w') as file:
                file.write(e)

            # waiting to give time to device react
            sleep(1)

        # error handling while ssh connection
        except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
            print(error)
            print(decorator_1)