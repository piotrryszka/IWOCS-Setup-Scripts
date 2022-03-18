# FUNCTIONS USED IN SCRIPT

# imports
import os
from datetime import datetime
from prettytable import PrettyTable as pt
import subprocess

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
    # printing table with devices
    tb = pt()
    # add headers
    tb.field_names = ["ID", "Device", "UDI", "License", "Status", "Expiration", "OK"]
    #returning table
    return tb

# adding rows to our conf license table with devices
# TODO: need to add more arguments
def adding_row(table, count, device):
    table.add_row([count,f"{device}", "IE-4010-4S24P:FDO2250U0AV",'ipservices', "Active, in use", "Pernament", "OK"])
    count+=1
    return count