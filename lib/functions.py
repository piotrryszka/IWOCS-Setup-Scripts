# FUNCTIONS USED IN SCRIPT

# imports
import os
from datetime import datetime
from prettytable import PrettyTable as pt
import subprocess
from pythonping import ping
from time import sleep

from config.data import decorator_1, count_ping, ip_hub, dict_ip, sleep_time, finish_time


# printing accessible logs
def printing_logs(lang_dict):
    files = os.listdir('logs/console_logs')
    # printing files
    print(lang_dict['print_logs'])
    print(*files, sep = ', ')

# creating_timestamp to make logs clearer
def creating_timestamp(lang_dict):
    # datetime object containing current date and time
    now = datetime.now()
    # converting data object to string
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(f"{lang_dict['timestamp']}", dt_string)

# starting tftp server to download config to device
def start_tftp(lang_dict):
    print(lang_dict['tftp_start'])
    print(decorator_1)
    subprocess.Popen([r"tftp-server/tftpd32.exe"])

# instruction to set tftp server properly
def user_tftp(lang_dict):
    continue_flag = True
    print(lang_dict['tftp_folder'])
    print(decorator_1)
    # user input if everything is set properly
    while continue_flag:
        user_input = input(lang_dict['tftp_ready'])
        print(user_input)
        print(decorator_1)
        if user_input =='1':
            print('Everything was set, you can continue...')
            print(decorator_1)
            continue_flag = False
        else:
            print(lang_dict['bad_conf_ip'])
            print(decorator_1)

# final tftp check before uploading config files
def final_tftp():
    output_netstat = str(subprocess.check_output("netstat -na | findstr /R ^UDP", shell=True)).strip()
    check_string = 'UDP    0.0.0.0:69'
    # checking if server works, use return in for example while loop
    if check_string in output_netstat:
        return True
    else:
        return False

# informing user to connect the console cable
def check_com(lang_dict):
    running_flag = True
    while running_flag:
        print(lang_dict['com_cable'])
        user_choice = input(lang_dict['com_accept'])
        print(user_choice)
        print(decorator_1)
        if user_choice == '1':
            running_flag = False
        else:
            pass

# good order of restarting devices
def order_dev(conf_devices_list, device_order, new_dict, order_dev_dict):
    # looking for the correct order of restarting devices
    for k in order_dev_dict:
        for y in device_order:
            if k == y:
                new_dict[device_order.index(k)] = {'device': k, 'ip': f'172.30.100.{order_dev_dict[k]}'}
    # creating new empty dict to return it to the main.py
    test_dict = {}

    # filling new dict
    for key in sorted(new_dict):
        test_dict[key] = new_dict[key]

    return test_dict

# printing already initial configured devices
def list_dev(device_list, lang_dict):
    device_list = list(dict.fromkeys(device_list))
    if len(device_list)>0:
        print(lang_dict['listing_dev'])
        print(*device_list, sep=', ')
        print(decorator_1)
    else:
        pass

# creating basic table with headers from scratch
def create_table():
    tb = pt()
    # add headers
    tb.field_names = ["ID", "Device", "UDI", "License", "Status", "Expiration", "OK"]
    # returning table
    return tb

# adding rows to our conf license table with devices
def adding_row(table, count, device, udi, type_license, status_license, time_license, ok):
    table.add_row([count, device, udi, type_license, status_license, time_license, ok])
    count+=1
    return count

# closing tftp server application
def kill_tftp():
    try:
        # stdout/stderr argument forbid to print on console output and error output
        subprocess.call(["taskkill","/F","/IM","tftpd32.exe"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except:
        pass

# closing putty application
def kill_putty(decision):
    if decision == '1':
        try:
            # stdout/stderr argument forbid to print on console output and error output
            subprocess.call(["taskkill","/F","/IM","puTTY.exe"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except:
            pass

def create_table_ver(lang_dict):
    tb = pt()
    # add headers
    tb.title = lang_dict['ver_table']
    tb.field_names = ["ID", "Name", "Model", "Current Version", "New Version"]
    # returning table
    return tb

# adding rows in version table
def add_row_ver(table):
    with open('temp/version.txt', 'r') as text_file:
        for line in text_file:
            version_list = line.split()
            table.add_row(version_list)

# function to prepare which device need to be updated
def prepare_software(lang_dict):
    counter = 0
    # flag to be updated to leave loop
    update_flag = True
    while update_flag:
        # question to user if he want to update sth
        print(decorator_1)
        user_update = input(lang_dict['ver_update'])
        print(user_update)
        print(decorator_1)
        if user_update == '1':
            counter += 1
            update_list = []
            # empty list to return devices
            # question which devices user wants to update
            user_dev_list = list(map(str, input(lang_dict['ver_dev']).split()))
            user_dev_list = list(dict.fromkeys(user_dev_list))
            print(*user_dev_list, sep=', ')
            print(decorator_1)
            # reading possible devices from version txt file
            with open('temp/version.txt') as file:
                new_list = []
                data = file.readlines()
                # stripping data
                stripped_data = [e.strip() for e in data]
                # splitting data into small elements
                for element in stripped_data:
                    element = element.split(' ')
                    new_list.append(element)
                # checking if the device is correct
                for x in new_list:
                    if x[0] in user_dev_list:
                        update_list.append(x)
            update_flag = False
        else:
            update_flag = False
    if counter == 0:
        update_list = []
    # returning list with the devices needs to be updated
    return update_list

# checking if the device is available by ping
def check_ping(lang_dict):
    # empty string
    result = ''
    # creating table
    tb = pt()
    # add header
    tb.title = lang_dict['ping_tab']
    # add columns
    tb.field_names = ["Name", "IP Address", "PING Status"]
    # opening txt file with device name and ip address
    with open('temp/already_conf.txt', 'r') as file:
        lines = file.readlines()
        # stripping lines
        stripped = [s.strip() for s in lines]
        print(lang_dict['ping_wait'])
        for element in stripped:
            # splitting element in line
            new_strip = element.split(' ')
            # setting parameters to function, sending 1 ICMP packet
            ping_output = ping(f'172.30.100.{new_strip[1]}', count=count_ping)
            for response in ping_output:
                # printing dots to console to make sure that something is happening in script
                print('.', end='')
                # checking if the ping was successful
                if response.error_message is None:
                    result = "OK"
                else:
                    result = " "
                # adding rows
                tb.add_row([new_strip[0],f'172.30.100.{new_strip[1]}', result])
    print(decorator_1)
    print(decorator_1)
    print(tb)
    # returning table to save it to file
    return tb


# function to test correctness of licenses of different network devices
def check_license(udi, state_string, type_string, ipservices_string):
    # checking for IE4010
    if state_string == 'Active, In Use' and type_string == 'PermanentRightToUse' and ipservices_string == 'ipservices' and 'IE-4010' in udi:
        ok_not = 'OK'
    # checking for IE2000
    elif state_string == 'Active, In Use' and type_string == 'Permanent' and ipservices_string == 'iplite' and 'IE-2000' in udi:
        ok_not = 'OK'
    # handling problem with reading one of the variables
    elif state_string == 'UNKNOWN' or type_string == 'UNKNOWN' or ipservices_string == 'UNKNOWN':
        ok_not = "UNKNOWN"
    else:
        ok_not = "NOT-OK"
    # returning variable tu put in the table
    return ok_not

# function to create proper directories for different devices
def create_dir(name_dev, lang_dict):
    # create directories
    dirName = name_dev
    try:
        # create target Directory
        os.mkdir(f'support/show-tech/{dirName}')
    # error handling
    except FileExistsError:
        print(lang_dict['dir_exists'] , dirName)
        print(decorator_1)
    except:
        print(lang_dict['unknown_error'])
        print(decorator_1)

# TODO: needs upgrading
# pinging hub ip address
def check_hub_ping():
    ping_status = False
    ping_output = ping(f'{ip_hub}', count=count_ping)
    for response in ping_output:
        # printing dots to console to make sure that something is happening in script
        print('.', end='')
        # checking if the ping was successful
        if response.error_message is None:
            # ping works, device could be reached
            ping_status = True
    # TODO: need to be done later
    # returning status of ping
    return ping_status

# checking project config connection by ping
def ping_projects(lang_dict, dict_dev):
    # printing prompt what is done now
    print(lang_dict['current_ping'])
    # creating pretty table object and configuring it
    tb = pt()
    # adding name of columns
    tb.field_names = ['Name of device', 'IP', 'Status']
    # adding title to pretty table
    tb.title = 'Checking connection to project configs'
    for k in reversed(dict_dev.keys()):
        # sending ping
        ping_output = ping(f"{dict_ip[dict_dev[k]['device']]}", verbose=False, count=count_ping)
        # printing dots to console to make sure that something is happening in script
        print('.', end='')
        for response in ping_output:
            # printing dots to console to make sure that something is happening in script
            print('.', end='')
            # checking if the ping was successful
            if response.error_message is None:
                # ping works, device could be reached
                ping_status = 'OK'
            else:
                ping_status = " "
        tb.add_row([dict_dev[k]['device'], dict_ip[dict_dev[k]['device']], ping_status])
    print(decorator_1)
    print(decorator_1)
    # printing tb table to console
    print(tb)
    print(lang_dict['check_ping'])
    print(decorator_1)

    # saving table to txt file
    dateTimeObj = datetime.now()
    dateObj = dateTimeObj.date()
    timeObj = dateTimeObj.time()
    dateStr = dateObj.strftime("%d.%m.%Y")
    timeStr = timeObj.strftime("%Hh-%Mm")
    with open(f'support/info_tables/ping_project/ping-project-check-{dateStr}-{timeStr}.txt', 'w') as f:
        f.write(str(tb))

# checking if the device has booted after downloading project config
def check_booting_ping(lang_dict, dict_dev):
    # flag to run function
    running_flag = True
    # counter of time
    count_time = 0
    # temporary list to be filled with ip addresses
    temporary_list = []

    # adding address to temporary list
    for k in reversed(dict_dev.keys()):
        temporary_list.append(dict_ip[dict_dev[k]['device']])

    print(lang_dict['ping_project'])

    while running_flag and count_time <= finish_time:
        for ip_add in temporary_list:
            # pinging by ip address already configured devices
            ping_output = ping(f"{ip_add}", verbose=False, count=count_ping)
            for response in ping_output:
                # printing dots to console to make sure that something is happening in script
                print('.', end='')
                # checking if the ping was successful
                if response.error_message is None:
                    # deleting ip address to ping
                    temporary_list.remove(ip_add)
            if len(temporary_list) == 0:
                running_flag = False
                break
        # adding time to counter of time
        count_time += sleep_time
        # sleep function
        sleep(sleep_time)
    print(decorator_1)
    print(decorator_1)

# pinging by initial ip addresses
def ping_initial():
    with open('temp/already_conf.txt', 'r') as file:
        # dic with ip addresses
        final_dic = {}
        running_flag = True
        # reading file to structure
        for line in file:
            list_license = line.split()
            final_dic[list_license[0]] = f'172.30.100.{list_license[1]}'
        while running_flag:
            for k in list(final_dic):
                # sending ping
                ping_output = ping(final_dic[k], verbose=False, count=count_ping)
                # # printing dots to console to make sure that something is happening in script
                print('.', end='')
                for response in ping_output:
                    # printing dots to console to make sure that something is happening in script
                    print('.', end='')
                    # checking if the ping was successful
                    if response.error_message is None:
                        # ping works, device could be reached
                        # deleting element of dictionary
                        del final_dic[k]
                    else:
                        pass
                # checking if all devices are pinging
                if len(final_dic) == 0:
                    # leaving loop
                    running_flag = False