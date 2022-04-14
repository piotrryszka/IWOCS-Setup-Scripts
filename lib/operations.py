# FUNCTIONS WORKING ON TXT FILES

# imports
import os
from os import listdir
from os.path import isfile, join
from datetime import datetime
from time import sleep

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
    return f'support/license-check-{dateStr}-{timeStr}.txt'

# saving info about devices and their license to file
def saving_info_lic(counter_table, user_device, udi, license, status, expiration, ok):
    with open('temp/licenses.txt', 'a') as file:
        file.write(f'{counter_table} {user_device} {udi} {license} {status} {expiration} {ok}')
        file.write('\n')
        counter_table += 1
        return counter_table

# reading info about license from txt file
def reading_license(conf_table):
    with open('temp/licenses.txt', 'r') as file:
        for line in file:
           list_license = line.split()
           counter_table = adding_row(conf_table,int(list_license[0]),list_license[1], list_license[2], list_license[3], ''.join(list_license[4:-2]), list_license[-2], list_license[-1])

# deleting device logs
def deleting_dev_logs():
    files = os.listdir('logs/device_logs')
    # deleting files
    for file in files:
        # cannot delete the file from today's date
        try:
            os.remove(f'logs/device_logs/{file}')
        except:
            pass

# deleting table with licenses and their status for support
def deleting_dev_license():
    files = os.listdir('support')
    # deleting files
    for file in files:
        # cannot delete the file from today's date
        try:
            os.remove(f'support/{file}')
        except:
            pass

# collecting license data from device
def download_license(ser = 'COM1'):
    # crating empty strings
    state_string = ''
    type_string = ''
    ipservices_string = ''

    try:
        # waiting for the device to finish reading commands from initial config
        print(".............................................")
        sleep(15)

        # sending two commands to go into privilege mode
        send_to_console(ser, '\n')
        send_to_console(ser, 'en')
    except:
        pass

    # try and except to not fail during the script and arguments

    # sending command to get UDI
    try:
        e = send_to_console(ser, 'sh license udi', 0.5)
        li = list(e.split())
        # udi data
        udi = li[11]
    except:
        udi = "UNKNOWN"

    # checking license and its status
    try:
        e = send_to_console(ser, 'sh license', 2)

        # creating temporary txt file
        with open("temp/license_console.txt", "w") as text_file:
            text_file.write(e)

        # empty list
        list_of_lists = []

        # reading temporary txt file
        with open('temp/license_console.txt', 'r') as f:
            counter =0
            lines = f.readlines()
            for line in lines:
                if counter < 1:
                    if 'License State:' in line:
                        line_read = line.split()
                        our_info = line_read[2:]
                        state_string = ' '.join(our_info)
#                         print(state_string)
                    if 'License Type:' in line:
                        line_read = line.split()
                        our_info = line_read[2:]
                        type_string = ' '.join(our_info)
#                         print(state_string)
                    if 'ipservices' in line:
                        line_read = line.split()
                        our_info = line_read[3:]
                        ipservices_string = ' '.join(our_info)
#                         print(ipservices_string)
                if 'lanbase' in line:
                    counter =+1
    except:
        state_string = 'UNKNOWN'
        type_string = 'UNKNOWN'
        ipservices_string = 'UNKNOWN'

    # returning 4 strings to be used in license table
    return udi, state_string, type_string, ipservices_string

# sending sh_version command and saving it output to txt file
def sh_version(ser):
    # sending command
    output = send_to_console(ser, 'sh version', 2)
    # saving output to txt file
    with open('temp/info_ver.txt', 'w') as file:
        file.write(output)

# reading info about version from txt file
def read_version(id, user_device):
    with open('temp/info_ver.txt', 'r') as my_file:
        for line in my_file:
            # looking for actual software version
            if 'Version' in line:
                my_list = line.split(',')
                for x in my_list:
                    if 'Version' in x:
                        x = x.strip()
                        x = x.split(' ')
                        act_version = x[-1]
            # looking for actual device model
            if 'System image file' in line:
                my_list = line.split(' ')
                for x in my_list:
                    if 'flash' in x:
                        x = x.split('/')
                        x = x[1].split('-')
                        # printing device model
                        final_device = x[0]
    # TODO: dodac try itp
    # reading possible
    # change it later, because path would be different
    files = os.listdir('firmware/ie4010')
    # adding first file to an argument
    file = str(files[0])
    string_file = file
    # saving data to txt file
    with open('temp/version.txt', 'a') as file:
        file.write(f'{id} {user_device} {final_device} {act_version} {string_file}')
        file.write('\n')

# saving version table to txt
def saving_ver_table(table):
    dateTimeObj = datetime.now()
    dateObj = dateTimeObj.date()
    timeObj = dateTimeObj.time()
    dateStr = dateObj.strftime("%d.%m.%Y")
    timeStr = timeObj.strftime("%Hh-%Mm")
    with open(f'support/version-check-{dateStr}-{timeStr}.txt', 'w') as f:
        f.write(str(table))

# adding ip to the already configured devices to update software
def add_ip(dev_list):
    with open('temp/already_conf.txt') as file:
        lines = file.readlines()
        stripped = [s.strip() for s in lines]
        for element in stripped:
            new_strip = element.split(' ')
            for name in dev_list:
                if new_strip[0] == name[1]:
                    name.append(f'172.30.100.{new_strip[1]}')
    return dev_list

# saving ping table to txt
def saving_ping_table(table):
    dateTimeObj = datetime.now()
    dateObj = dateTimeObj.date()
    timeObj = dateTimeObj.time()
    dateStr = dateObj.strftime("%d.%m.%Y")
    timeStr = timeObj.strftime("%Hh-%Mm")
    with open(f'support/ping-check-{dateStr}-{timeStr}.txt', 'w') as f:
        f.write(str(table))