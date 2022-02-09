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
    subprocess.Popen([r"tftp-server/tftpd64.exe"])