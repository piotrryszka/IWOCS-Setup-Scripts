# COMMANDS WORKING ON DEVICES

# imports
from serial import Serial
from time import sleep
import subprocess
import os
from datetime import datetime

from config.data import ie2000, ie4010, decorator_1

# sending commands to console
def send_to_console(ser_fun: Serial, command: str, wait_time: float = 0.2):
    command_to_send = command + "\r\n"
    ser_fun.write(command_to_send.encode('utf-8'))
    sleep(wait_time)
    return ser_fun.read(ser_fun.inWaiting()).decode('utf-8')

# counting gigabit and fast ports in devices
def checking_switch_ports(ser_port):
    send_to_console(ser_port, 'no')
    send_to_console(ser_port, 'en')
    send_to_console(ser_port, 'term len 0')
    checking_string = ''
    checking_string += send_to_console(ser_port, 'sh run', 5)
    checking_string += send_to_console(ser_port, '\n')
    number_gigabit = checking_string.count('GigabitEthernet')
    number_fast = checking_string.count('FastEthernet')
    port_dictionary = {'Gigabit': number_gigabit,
                       'Fast': number_fast
                        }
    send_to_console(ser_port, 'term len 24')
    return port_dictionary

# checking if ip address was properly set by user
def checking_ip_address(lang_dict):
    print(lang_dict['ip_prompt'])
    print(decorator_1)
    user_input = input(lang_dict['ready_ip'])
    print(user_input)
    print(decorator_1)
    IP_flag = False
    continue_flag = True
    while continue_flag:
        if user_input == "1":
            output_ipconfig = str(subprocess.check_output("ipconfig /all", shell=True)).strip()
            ip_address = '172.30.100.91'
            if ip_address in output_ipconfig:
                IP_flag = True
                print(lang_dict['good_ip'])
                break
            else:
                IP_flag = False
                print(lang_dict['again_ip'])
            continue_flag = False
        else:
            print(lang_dict['bad_conf_ip'])
            break
    return IP_flag

# checking type of device
def checking_device(ser_port, user_device, lang_dict):
    good_conf = False
    check_device = send_to_console(ser_port, 'sh lic udi')
    # routers/firewall
    # TODO: to code here some lists
    print(decorator_1)
    print(decorator_1)

    # TODO here change check it
    if 'IE-4010' in check_device:
        if user_device in ie4010:
            print(lang_dict['proper_device'])
            good_conf = True
        else:
            print(lang_dict['bad_device'])
    elif 'IE-2000' in check_device:
        if user_device in ie2000:
            print(lang_dict['proper_device'])
            good_conf = True
        else:
            print(lang_dict['bad_device'])
    return good_conf

# checking if tftp server is already running
def check_tftp(lang_dict):
    print(decorator_1)
    print(lang_dict['tftp_server'])
    working_flag = False
    continue_flag = True
    while continue_flag:
        print(decorator_1)
        user_input = input(lang_dict['tftp_check'])
        print(user_input)
        print(decorator_1)
        if user_input == '1':
            output_netstat = str(subprocess.check_output("netstat -na | findstr /R ^UDP", shell=True)).strip()
            # string to be found in cmd output
            check_string = 'UDP    0.0.0.0:69'
            if check_string in output_netstat:
                print(lang_dict['tftp_occupied'])
                print(decorator_1)
                working_flag = True
            else:
                print(lang_dict['tftp_free'])
                print(decorator_1)
                working_flag = False
                continue_flag = False
            return working_flag
        else:
            continue_flag = True
            print(lang_dict['bad_conf_ip'])
            print(decorator_1)

# going to conf mode before handling initial configuration
def to_conf_mode(ser_port):
    commands_list = ['en', 'conf t']
    for com in commands_list:
        send_to_console(ser_port, com)

