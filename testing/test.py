# #TODO:
# # THREADS
# import _thread
# import time
# import threading
#
# # Define a function for the thread
# def print_time( threadName, delay):
#    count = 0
#    while count < 5:
#       time.sleep(delay)
#       count += 1
#       print ("%s: %s" % ( threadName, time.ctime(time.time()) ))
#
# def print_star(delay):
#     while 1:
#         time.sleep(delay)
#         print('*', end='')
#
# def counting_process(delay):
#     while 1:
#         time.sleep(delay)
#         e = threading.active_count()
#         print(e)
#
#
#
# # Create threads as follows
# try:
#    _thread.start_new_thread( print_time, ("Thread-1", 1, ) )
#    _thread.start_new_thread( print_time, ("Thread-2", 1, ) )
#    _thread.start_new_thread(print_star, (0.5,))
#    _thread.start_new_thread(counting_process, (2,))
#    e = threading.active_count()
#    print(e)
#
# except:
#    print ("Error: unable to start thread")
#
#
# while 1:
#    pass
# reading temporary txt file
import os
from os import listdir
from os.path import isfile, join
from datetime import datetime
from time import sleep

from config.data import decorator_1
from lib.commands import send_to_console
from lib.functions import adding_row

def download_license(ser = 'COM7'):
    # crating empty strings
    state_string = ''
    type_string = ''
    ipservices_string = ''

    try:
        # waiting for the device to finish reading commands from initial config, need to be tested how long it should be
        sleep(15)

        # sending two commands to go into privilege mode
        send_to_console(ser, '\n')
        send_to_console(ser, 'en')
    except:
        pass

    # try and except to not fail during the script and arguments

    # sending command to get UDI
# try:
    e = send_to_console(ser, 'sh license udi', 0.5)
    print(e)
    li = list(e.split())
    # udi data
    udi = li[11]
# except:
    udi = "UNKNOWN"

    # checking license and its status
    try:
        e = send_to_console(ser, 'sh license', 2)

        # creating temporary txt file
        with open("temp/license_console.txt", "w") as text_file:
            text_file.write(e)

        # reading temporary txt file
        with open('temp/license_console.txt', 'r') as f:
            counter =0
            lines = f.readlines()
            print(lines)
            for line in lines:
                if counter < 1:
                    if 'License State:' in line:
                        line_read = line.split()
                        our_info = line_read[2:]
                        state_string = ' '.join(our_info)
                        print(state_string)
                    if 'License Type:' in line:
                        line_read = line.split()
                        our_info = line_read[2:]
                        type_string = ' '.join(our_info)
                        print(state_string)
                    if 'ipservices' in line:
                        line_read = line.split()
                        our_info = line_read[3:]
                        ipservices_string = ' '.join(our_info)
                        print(ipservices_string)
                if 'lanbase' in line:
                    counter =+1
    except:
        state_string = 'UNKNOWN'
        type_string = 'UNKNOWN'
        ipservices_string = 'UNKNOWN'

    # returning 4 strings to be used in license table
    return udi, state_string, type_string, ipservices_string

e = download_license('COM7')
print(e)