# imports
from serial import Serial
from time import sleep
from lib.commands import send_to_console, checking_switch_ports, checking_ip_address, checking_device, check_tftp, to_conf_mode
from lib.operations import opening_device_list, reading_conf_files, creating_proper_configuration, deleting_files, listing_conf, deleting_conf
from lib.booting import checking_booting
from lib.languages import listing_languages, reading_language
from lib.data import ip_number, decorator_1
from lib.logging import *
from lib.network import ssh_con
from lib.functions import printing_logs, creating_timestamp, start_tftp, user_tftp, final_tftp, printing_confs
import sys

# Program flags:
running_flag = True  # main flag, running program
system_flag = True  # flag about type of system
com_flag = True  # flag checking COM
device_flag = True  # flag checking device
user_boot_flag = True # flag checking if device chosen by user is booted
ip_flag = False # flag if ip is correctly set by user
proper_language = False # flag if the language chosen by user is possible to be used
del_flag = False # flag to check what user want to do after deleting logs
tftp_flag = True # flag to check if the port UDP 69 is taken
ssh_flag = True # flag to configure devices by ssh connections
check_flag = True # flag to check if ip address is available

# FIXED Variables:
COM_speed = 9600 # serial port speed
ip_list = [] # empty list later filled with ip addresses
conf_device_list = [] # empty list later filled with project configs downloaded
list_devices = [] # empty dictionary to be filled with ip addresses and devices

# main project
while running_flag:
    # choosing language
    while not proper_language:
        print("Available languages are presented below:")
        languages = listing_languages()
        print(*languages, sep = ', ')
        user_language = input("Please choose one of possible languages: ").title()
        print(user_language)
        if user_language in languages:
            proper_language = True
            # making a list dictionary with expressions in chosen language
            lang_expressions = reading_language(user_language)
        elif user_language == "0":
            lang_expressions = reading_language('En')
            proper_language = True
        else:
            print("You have provided wrong language, try again...")
        print(decorator_1)

    # creating_timestamp
    creating_timestamp(lang_dict=lang_expressions)
    print(decorator_1)

    # info to user how to leave any part of program
    print(lang_expressions['information_prompt'])
    print(decorator_1)

    # deleting logs
    printing_logs(lang_expressions)
    user_del = input(lang_expressions['deleting_logs'])
    del_flag = deleting_files(lang_dict = lang_expressions, user_input = user_del)
    print(user_del)
    if del_flag == True:
        print(lang_expressions['del_info'])
        break
    else:
        pass

    # question about complete system or one module TASK 184
    print(decorator_1)
    user_system = input(lang_expressions['module_question']).lower()
    print(user_system)
    print(decorator_1)
    if user_system == '1':
        while com_flag:
            # question about which COM port is user using TASK 185
            user_COM = input(lang_expressions['port_question']).lower()
            print(user_COM)
            print(decorator_1)
            if user_COM.isnumeric() and user_COM != '0':

                # Creating string for connection to the device
                COM_string = "COM" + user_COM

                print(decorator_1)

                # Creating a list with all the possible devices
                device_list = opening_device_list(file_name = 'project_names_of_devices.txt')

                while device_flag:
                    # User chooses the device, which one he wants to
                    choosing_device = True
                    while choosing_device == True:
                        user_device = input(lang_expressions['device_question']).upper()
                        print(user_device)
                        user_list = []
                        for dev in device_list:
                            if user_device in dev:
                                user_list.append(dev)
                        print(decorator_1)
                        print(lang_expressions['listing_devices'])
                        print(*user_list, sep=', ')
                        print(decorator_1)
                        if user_device in user_list:
                            choosing_device = False

                    # Checking if the device is in the list of devices
                    if user_device in device_list:
                        print(decorator_1)
                        print(lang_expressions['user_choice'])
                        print(f"{COM_string} ----> {user_device}")
                        print(lang_expressions['wait_prompt'])
                        print(decorator_1)

                        # TODO for tests it is commented (TRY AND EXCEPT)
                        # TODO: move all commands one tab
#                         try:

                        # connection set
                        ser = Serial(COM_string, COM_speed)

                        # waiting for router/switch to boot
                        user_boot_flag = checking_booting(port = ser)

                        # counting number of gigabit and fast ports
                        device_ports = checking_switch_ports(ser_port = ser)

                        # checking if device is really the device, which was wanted by user
                        proper_device = checking_device(ser_port = ser, user_device = user_device, lang_dict = lang_expressions)

                        # TODO: needs to be commented
                        # returning next ip number and full name of configured device to download to specified device
                        our_conf = creating_proper_configuration(user_device = user_device, port_num = device_ports['Gigabit'], ip_add = ip_number)

                        # adding current ip address to list
                        ip_list.append(f'172.30.100.{ip_number}')

                        # returning tuple with full name device and next iip number to bes used
                        actual_device = our_conf[1] # name of device
                        ip_number = our_conf[0] # new ip address incremented by +1

                        # addding full device name with ip address to the list
                        list_devices.append(actual_device)
                        print(list_devices)

                        # TODO: DELETE IT
                        # need to be deleted
#                         user_boot_flag = True
#                         proper_device = True

                        if user_boot_flag and proper_device:

                            print(lang_expressions['not_configured'])
                            print(decorator_1)

                            # going to configuration mode
                            to_conf_mode(ser)

                            # opening file with configuration
                            actual_device = actual_device
                            stripped_list = reading_conf_files(file = actual_device)

                            # executing commands from the list
                            for command in stripped_list:
                                pass
                                send_to_console(ser, command)
                                # printing dots to inform user that script is still working
                                print('.', end='')

                            print(decorator_1)
                            print(decorator_1)
                            # closing connection
                            ser.close()
                            print(f"{lang_expressions['proper_conf']}{user_device}.")

                            # TODO: Uncomment it
                            # print(f"{lang_expressions['close_con']}{ser.name}.")
                            print(decorator_1)

                            # question if user has finished initial configuration of devices
                            finish_conf = input(lang_expressions['finish_conf'])
                            print(finish_conf)
                            print(decorator_1)
                            if finish_conf == '1':
                                # exit the COM connections
                                device_flag = False
                                com_flag = False
                            else:
                                # configuring next device
                                device_flag = True
                                pass

                    # TODO: needs to be uncommented
                        else:
                            print(lang_expressions['start_conf'])
                            print(lang_expressions['again_prompt'])
                            print(decorator_1)
                            # closing connection
                            ser.close()
                            print(f"{lang_expressions['close_con']}{ser.name}.")
                            print(decorator_1)
                            break
                            # TODO: UNCOMMENT
#                         except:
                        # bad chosen device or it is not working
                        print(lang_expressions['not_working'])
                        print(decorator_1)

                    elif user_device == str(0):
                        break
                    else:
                        print(lang_expressions['not_supported'])

            # leaving script by '0' input
            elif user_COM == str(0):
                break
            else:
                # bad user input about COM port
                print(lang_expressions['not_number'])

        # SSH CONNECTIONS
        else:
            print(lang_expressions['ssh_move'])

            # TODO: UNCOMMENT
            # checking ip address but need to be commented
#             while ip_flag == False:
#                 ip_set = checking_ip_address(lang_dict = lang_expressions)
#                 if ip_set == True:
#                     ip_flag = True

            # checking if server tftp is already running
            while tftp_flag:
                tftp_flag = check_tftp(lang_dict = lang_expressions)

            # starting TFTP server
            start_tftp(lang_dict = lang_expressions)

            # user instructions to set config of TFTP Server
            user_tftp(lang_dict = lang_expressions)

            # checking if server is running
            working_tftp = final_tftp()

            # SSH connection established
            print(lang_expressions['waiting_ssh'])

            # waiting 10 seconds to get configuration ready
            print(decorator_1)

            # information prompt about good order of restarting TFTP
            print(lang_expressions['warning_order'])
            print(decorator_1)

            # printing all possible configurations created by the user and the script
            print(lang_expressions['ready_dev'])
            print(*list_devices, sep = ', ')
            print(decorator_1)

            # SSH CONFIGURATION LOOP
            while ssh_flag and working_tftp:

                # choosing proper configuration
                while check_flag:
                    # printing ip addresses
                    print(lang_expressions['ip_connect'])
                    print(*ip_list, sep=', ')
                    print(decorator_1)
                    # taking IP input from user
                    new_host = input(lang_expressions['ip_add'])
                    print(new_host)
                    print(decorator_1)
                    # checking if ip is available
                    if new_host in ip_list:
                        # removing ip address
                        ip_list.remove(new_host)
                        print(f"{lang_expressions['proper_ip']}{new_host}")
                        print(decorator_1)
                        break
                    else:
                        print(lang_expressions['bad_ip'])
                        print(decorator_1)

                # listing possible confs to download to the device with prompts
                user_conf = listing_conf(lang_dict = lang_expressions)

                # adding device to the already configured list
                conf_device_list.append(user_conf)

                # printing devices which are already configured
                print(lang_expressions['already_conf'])
                if len(conf_device_list) > 0:
                    print(*conf_device_list, sep=', ')
                    print(decorator_1)
                else:
                    print(lang_expressions['no_devices'])
                    print(decorator_1)

                # connection with specified by user IP address and project configuration
                ssh_con(file = user_conf, host = new_host)

                # question about finishing configuration by TFTP and SSH
                user_fin = input(lang_expressions['user_finish'])
                print(user_fin)
                if user_fin == '1':
                    ssh_flag = False
                    print(decorator_1)
                    # commented because thank you phrase is also later
#                     print(lang_expressions['thank_you'])
#                     print(decorator_1)
                    running_flag = False
                    break
                else:
                    pass
    else:
        print(lang_expressions['not_complete'])
        running_flag = False


# LAST COMMANDS IN SCRIPT
# final question after whole script is finished
user_del_conf = input(lang_expressions['del_conf_question'])
print(user_del_conf)
print(decorator_1)
deleting_conf(lang_dict = lang_expressions, user_input = user_del_conf)

