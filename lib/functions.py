# FUNCTIONS USED IN SCRIPT

# imports
import os
from datetime import datetime
import subprocess
from lib.data import decorator_1


# printing accessible logs
def printing_logs(lang_dict):
    files = os.listdir('logs')
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
    print(lang_dict['tftp_ip'])
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

# printing accessible project configurations
def printing_confs(lang_dict):
    files = os.listdir('tftp-conf-files')
    # printing files
    print(lang_dict['conf_files'])
    print(*files, sep = ', ')

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