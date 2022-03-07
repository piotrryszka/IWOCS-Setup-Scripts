# FUNCTIONS WORKING ON TXT FILES

# imports
import os
from os import listdir
from os.path import isfile, join

from lib.data import decorator_1
from lib.commands import send_to_console

# opening possible devices to configure
def opening_device_list(file_name):
    with open(f'static_files/{file_name}', 'r') as file_devices:
                        lines = file_devices.read()
                        list_of_lists = lines.splitlines()
                        return list_of_lists
                        file_devices.close()

# reading commands from files (add argument to make this happen)
def reading_conf_files(file):
    with open(f'user-configuration-files/{file}') as file:
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
        with open(f'user-configuration-files/cisco-switch-{user_device}-172.30.100.{str(ip_add)}', 'w') as file:
            for row in content_list:
                file.write(str(row) + '\n')
            # adding one to create a new IP ADDRESS
            ip_add +=1
        # returning tuple with new ip address and new file
        return ip_add, f'cisco-switch-{user_device}-172.30.100.{str(ip_add-1)} '

# deleting logs and handling logs files
def deleting_files(lang_dict, user_input):
    to_leave = False
    files = os.listdir('logs')
    # deleting files
    if user_input == '1':
        for file in files:
            # cannot delete the file from today's date
            try:
                os.remove(f'logs/{file}')
            except:
                pass
        return to_leave
    elif user_input == '0':
        to_leave = True
        return to_leave
    else:
        return to_leave

# listing project configurations and making a list
def listing_conf(lang_dict):
    running_flag = True

    # creating a list of project configs
    onlyfiles = [f for f in listdir('tftp-conf-files') if isfile(join('tftp-conf-files', f))]

    while running_flag:
        # listing configuration
        print(lang_dict['project_confs'])
        print(*onlyfiles, sep = ', ')
        print(decorator_1)
        user_choice = input(lang_dict['dev_conf'])
        print(user_choice)
        print(decorator_1)
        if user_choice in onlyfiles:
            running_flag = False
            return user_choice
        else:
            print(lang_dict['bad_conf_dev'])
            print(decorator_1)
            pass

# deleting initial configuration files created by the user while using script
def deleting_conf(lang_dict):
    to_leave = False
    files = os.listdir('user-configuration-files')
    # deleting files
    for file in files:
        # cannot delete the file from today's date
        try:
            os.remove(f'user-configuration-files/{file}')
        except:
            pass
    print(lang_dict['del_conf'])
    print(decorator_1)
    print(lang_dict['thank_you_v2'])

# saving already configured devices
def saving_dev(dev_name):
    with open('user-configuration-files/already_conf.txt', 'a') as f:
        f.write(dev_name)
        f.write('\n')

# listing already configured devices from the file
def list_saved_dev(lang_dict):
    try:
        with open('user-configuration-files/already_conf.txt', 'r') as file:
            content_list = file.readlines()
            stripped_list = [s.strip() for s in content_list]
            if len(stripped_list)> 0:
                print(lang_dict['dev_already_conf'])
                print(*stripped_list, sep=', ')
                # returning list with already_conf devices
                return stripped_list
            else:
                pass
    except:
        print(lang_dict['no_conf'])