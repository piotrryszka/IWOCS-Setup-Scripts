# SSH CONNECTIONS

# imports
from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException
from time import sleep
from datetime import datetime

from config.data import password, username, decorator_1, server_ip

# establishing SSH connection and downloading project configs
def ssh_con(file, host):
    """

    :param file: name of project configuration of the device
    :param host: initial ip address of the device
    :return: NULL
    """
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
    """

    :param host: project ip address
    :param device: device for example IE4010
    :param command: command sent to the device for example: sh run
    :return: NULL
    """
    # creating timestamp
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
        "session_log": f"logs/project_logs/{device}_{host}_{dateStr}.txt",
        # enabling waiting for the output much longer
        "fast_cli": False
    }
    with ConnectHandler(**cisco1) as net_connect:
        try:
            # assigning command to sending command
            our_command = command

            # changing length of terminal to catch commands
            net_connect.send_command('terminal length 0', cmd_verify=False)

            # sending 'enter' to clear CLI window
            net_connect.send_command('\n', cmd_verify=False)

            # command sent to network device
            if our_command == 'show tech':
                command_output = net_connect.send_command_expect(our_command, cmd_verify=False)
            else:
                command_output = net_connect.send_command(our_command, cmd_verify=False)

            # changing length of terminal to basic
            net_connect.send_command('terminal length 24', cmd_verify=False)

            # replacing spaces in command with - char
            command = command.replace(' ', '-')

            # opening file and saving an output to the file
            with open(f'support/show-tech/{device}/{command}___{dateStr}.txt', 'w') as file:
                file.write(command_output)

            # waiting to give time to device react
            sleep(1)

        # error handling while ssh connection
        except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
            print(error)
            print(decorator_1)

# collecting license data from device by ssh
def download_license_ssh(host):
    """

    :param host: initial ip address
    :return: NULL
    """
    # creating timestamp
    now = datetime.now()
    dateTimeObj = datetime.now()
    dateObj = dateTimeObj.date()
    dateStr = dateObj.strftime("%d.%m.%Y")
    # configuration of network device
    cisco1 = {
        "device_type": f"cisco_ios",
        "host": f"{host}",
        # enabling waiting for the output much longer
        "fast_cli": False,
        "username": f"{username}",
        "password": f'{password}'
    }
    # crating empty strings
    state_string = ''
    type_string = ''
    ipservices_string = ''
    try:
        # sending two commands to go into privilege mode
        with ConnectHandler(**cisco1) as net_connect:
            command_output = net_connect.send_command_expect('\n', cmd_verify=False)
            command_output = net_connect.send_command_expect('en', cmd_verify=False)
    except:
        pass

    # try and except to not fail during the script and arguments

    # sending command to get UDI
    try:
        with ConnectHandler(**cisco1) as net_connect:
            e = net_connect.send_command_expect('sh license udi', cmd_verify=False)
        li = list(e.split())
        # udi data
        udi = li[-1]
    except:
        udi = "UNKNOWN"

    # checking license and its status
    try:
        with ConnectHandler(**cisco1) as net_connect:
            e = net_connect.send_command_expect('sh license', cmd_verify=False)

        # creating temporary txt file
        with open("temp/license_console.txt", "w") as text_file:
            text_file.write(e)

        # reading temporary txt file
        with open('temp/license_console.txt', 'r') as f:
            counter = 0
            counter_ie2000 = 0
            lines = f.readlines()
            for line in lines:
                if 'IE-4010' in udi:
                    if counter < 1:
                        if 'License State:' in line:
                            line_read = line.split()
                            our_info = line_read[2:]
                            state_string = ' '.join(our_info)
                        if 'License Type:' in line:
                            line_read = line.split()
                            our_info = line_read[2:]
                            type_string = ' '.join(our_info)
                        if 'ipservices' in line:
                            line_read = line.split()
                            our_info = line_read[3:]
                            ipservices_string = ' '.join(our_info)
                if 'IE-2000' in udi:
                    if 'iplite' in line:
                        counter_ie2000 = 0
                    if counter_ie2000 == 0:
                        if 'License Type:' in line:
                            line_read = line.split()
                            our_info = line_read[2:]
                            type_string = ' '.join(our_info)
                        if 'License State:' in line:
                            line_read = line.split()
                            our_info = line_read[2:]
                            state_string = ' '.join(our_info)
                        if 'iplite' in line:
                            line_read = line.split()
                            our_info = line_read[3:]
                            ipservices_string = ' '.join(our_info)
                    if 'mrp-manager' in line:
                        counter_ie2000 += 1
                if 'lanbase' in line:
                    counter =+ 1
    except:
        state_string = 'UNKNOWN'
        type_string = 'UNKNOWN'
        ipservices_string = 'UNKNOWN'

    # returning 4 strings to be used in license table
    return udi, state_string, type_string, ipservices_string

# sending sh_version command and saving it output to txt file
def sh_version(host):
    """

    :param host: initial ip address
    :return: NULL
    """
    # creating timestamp
    now = datetime.now()
    dateTimeObj = datetime.now()
    dateObj = dateTimeObj.date()
    dateStr = dateObj.strftime("%d.%m.%Y")
    # configuration of network device
    cisco1 = {
        "device_type": f"cisco_ios",
        "host": f"{host}",
        # enabling waiting for the output much longer
        "fast_cli": False,
        "username": f"{username}",
        "password": f'{password}'
    }
    # sending command
    with ConnectHandler(**cisco1) as net_connect:
        output = net_connect.send_command_expect('sh version', cmd_verify=False)
    # saving output to txt file
    with open('temp/info_ver.txt', 'w') as file:
        file.write(output)
