# FUNCTIONS USED IN SCRIPT

# imports
import os
from datetime import datetime
from prettytable import PrettyTable as pt
import subprocess
from pythonping import ping

from config.data import decorator_1


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
    #returning table
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
    #returning table
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
            ping_output = ping(f'172.30.100.{new_strip[1]}', verbose=False, count = 1)
            for response in ping_output:
                # printing dots to console to make sure that something is happening in script
                print('.', end='')
                # checking if the ping was successful
                if response.error_message == None:
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