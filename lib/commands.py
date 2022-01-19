# functions

# imports
from serial import Serial
from time import sleep
from lib.data import ie2000, ie4010, decorator_1
import subprocess

# sending commands to console
def send_to_console(ser_fun: Serial, command: str, wait_time: float = 0.5):
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
    print(decorator_1)
    IP_flag = False
    continue_flag = True
    while continue_flag:
        if user_input == "1":
            output_ipconfig = str(subprocess.check_output("ipconfig", shell=True)).strip()
            ip_address = '10.83.6.83'
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
