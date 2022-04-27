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
#
# # NEED TO FINISH THREADS AS WELL
from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException
from time import sleep
from datetime import datetime

from config.data import password, username, decorator_1, server_ip

def ssh_download(host, device, command):
    # creating timestamp
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y")
    dateTimeObj = datetime.now()
    dateObj = dateTimeObj.date()
    dateStr = dateObj.strftime("%d.%m.%Y")
    # configuration of network device
    cisco1 = {
        "device_type": f"cisco_ios",
        "host": f"{host}",
        "username": f"{username}",
        "password": f'{password}',
        # session logger
        "session_log": f"../logs/project_logs/{device}_{host}_{dateStr}.txt"
    }
    with ConnectHandler(**cisco1) as net_connect:
        # assigning command to sending command
        our_command = command

        # sending 'enter' to clear CLI window
        net_connect.send_command('\n', cmd_verify=False)

        # command sent to network device
        command_output = net_connect.send_command(our_command, cmd_verify=False)
        sleep(5)
        # replacing spaces in command with - char
        command = command.replace(' ', '-')

        # opening file and saving an output to the file
        with open(f'../support/show-tech/{device}/{command}___{dateStr}', 'w') as file:
            file.write(command_output)

        print('eee')


        # error handling while ssh connection
    # except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
    #     print(error)
    #     print(decorator_1)

ssh_download('172.30.100.101', 'TDS-1_A', 'show run')