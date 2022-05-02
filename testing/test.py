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

import os
from datetime import datetime
from prettytable import PrettyTable as pt
import subprocess
from pythonping import ping
from time import sleep

from config.data import decorator_1, count_ping, ip_hub, dict_ip, sleep_time, finish_time


# checking if the device has booted after downloading project config
def check_booting_ping(dict_dev):
    # flag to run function
    running_flag = True
    # counter of time
    count_time = 0
    # temporary list to be filled with ip addresses
    temporary_list = []

    # adding address to temporary list
    for k in reversed(dict_dev.keys()):
        temporary_list.append(dict_ip[dict_dev[k]['device']])


    while running_flag and count_time <= finish_time:
        for k in reversed(dict_dev.keys()):
            # pinging by ip address already configured devices
            ping_output = ping(f"{dict_ip[dict_dev[k]['device']]}", verbose=False, count=count_ping)
            print(dict_ip[dict_dev[k]['device']])
            for response in ping_output:
                # printing dots to console to make sure that something is happening in script
                print('.', end='')
                # checking if the ping was successful
                if response.error_message is None:
                    # deleting ip address to ping
                    temporary_list.remove(dict_ip[dict_dev[k]['device']])
            if len(temporary_list) == 0:
                running_flag = False
                break
        # adding time to counter of time
        count_time += sleep_time
        # sleep function
        sleep(sleep_time)
    print(decorator_1)
    print(decorator_1)

dictionary_dev = {0: {'device': 'TDS-1_A', 'ip': '172.30.100.10'}, 1: {'device': 'TDS-1_B', 'ip': '172.30.100.11'},}


check_booting_ping(dict_dev=dictionary_dev)