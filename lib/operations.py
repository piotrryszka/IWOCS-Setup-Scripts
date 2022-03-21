# FUNCTIONS WORKING ON TXT FILES

# imports
import os
from os import listdir
from os.path import isfile, join
from datetime import datetime

from config.data import decorator_1
from lib.commands import send_to_console
from lib.functions import adding_row

# opening possible devices to configure
def opening_device_list(file_name):
    with open(f'static_files/{file_name}', 'r') as file_devices:
                        lines = file_devices.read()
                        list_of_lists = lines.splitlines()
                        return list_of_lists
                        file_devices.close()

# reading commands from files (add argument to make this happen)
def reading_conf_files(file):
    with open(f'temp/{file}') as file:
        # getting commands from list
        content_list = file.readlines()
        stripped_list = [s.strip() for s in content_list]
        return stripped_list

# creating and reading conf files
def creating_proper_configuration(user_device, port_num, ip_add):
    with open('initial-configuration-files/cisco-switch') as f:
        lines = f.read()
        content_list = lines.split('\n')
        for x in content_list:
            # changing hostname
            if x == 'hostname xxx':
                our_index = content_list.index(x)
                content_list[our_index] = f'hostname {user_device}'
            # changing interface for whole range
            if x == 'interface GigabitEthernet1/1':
                int_index = content_list.index(x)
                content_list[int_index] = f'interface range GigabitEthernet1/1-{str(port_num)}'
            # changing ip address
            if x == ' ip address x.x.x.x y.y.y.y':
                ip_index = content_list.index(x)
                content_list[ip_index] = f' ip address 172.30.100.{str(ip_add)} 255.255.255.0'
        with open(f'temp/cisco-switch-{user_device}-172.30.100.{str(ip_add)}', 'w') as file:
            for row in content_list:
                file.write(str(row) + '\n')
            # adding one to create a new IP ADDRESS
            ip_add +=1
        # returning tuple with new ip address and new file
        return ip_add, f'cisco-switch-{user_device}-172.30.100.{str(ip_add-1)} '

# deleting logs and handling logs files
def deleting_files(lang_dict, user_input):
    to_leave = False
    files = os.listdir('logs/console_logs')
    # deleting files
    if user_input == '1':
        for file in files:
            # cannot delete the file from today's date
            try:
                os.remove(f'logs/console_logs/{file}')
            except:
                pass
        return to_leave
    elif user_input == '0':
        to_leave = True
        return to_leave
    else:
        return to_leave

# deleting initial configuration files created by the user while using script
def deleting_conf(lang_dict):
    files = os.listdir('temp')
    # deleting files
    for file in files:
        # cannot delete the file from today's date
        try:
            os.remove(f'temp/{file}')
        except:
            pass
    print(lang_dict['del_conf'])
    print(decorator_1)
    print(lang_dict['thank_you_v2'])

# saving already configured devices
def saving_dev(dev_name):
    with open('temp/already_conf.txt', 'a') as f:
        f.write(dev_name)
        f.write('\n')

# listing already configured devices from the file
def list_saved_dev():
    new_dict = {}
    try:
        with open('temp/already_conf.txt', 'r') as file:
            for line in file:
               (key, val) = line.split()
               new_dict[key] = val
    except:
        pass
    return new_dict

# saving already configured devices with their license status
def saving_license(table):
    # get the date object from datetime object
    # creating timestamp
    dateTimeObj = datetime.now()
    dateObj = dateTimeObj.date()
    timeObj = dateTimeObj.time()
    dateStr = dateObj.strftime("%d.%m.%Y")
    timeStr = timeObj.strftime("%Hh-%Mm")
    with open(f'support/license-check-{dateStr}-{timeStr}.txt', 'w') as f:
        f.write(str(table))

# saving info about devices and their license to file
def saving_info_lic(counter_table, user_device):
    with open('temp/licenses.txt', 'a') as file:
        file.write(f'{counter_table} {user_device} UDI LICENSE STATUS EXPIRATION OK')
        file.write('\n')
        counter_table += 1
        return counter_table

# reading info about license from txt file
def reading_license(conf_table):
    with open('temp/licenses.txt', 'r') as file:
        for line in file:
           list_license = line.split()
           counter_table = adding_row(table = conf_table,count = int(list_license[0]), device = list_license[1])