# imports
from serial import Serial
from time import sleep
from lib.commands import send_to_console, checking_switch_ports, checking_ip_address, checking_device, deleting_files, printing_logs, creating_timestamp
from lib.operations import opening_device_list, reading_conf_files, creating_proper_configuration
from lib.booting import checking_booting
from lib.languages import listing_languages, reading_language
from lib.data import ip_number, decorator_1
from lib.logging import *
from lib.network import ip_connect
import sys


# Program flags:
running_flag = True  # main flag, running program
system_flag = True  # flag about type of system
COM_flag = True  # flag checking COM
device_flag = True  # flag checking device
user_boot_flag = True
ip_flag = False
proper_language = False

# FIXED Variables:
COM_speed = 9600


# main project
while running_flag:

    # choosing language
    # it has to be in english
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
    creating_timestamp(lang_expressions)
    print(decorator_1)

    # info to user how to leave any part of program
    print(lang_expressions['information_prompt'])
    print(decorator_1)

    # checking ssh connection
    ip_connect()



    # deleting logs
    printing_logs(lang_expressions)
    user_del = input(lang_expressions['deleting_logs'])
    deleting_files(lang_expressions,user_del)


    # question about complete system or one module TASK 184
    user_system = input(lang_expressions['module_question']).lower()
    print(user_system)
    print(decorator_1)
    if user_system == '1':
        while COM_flag:
            # question about which COM port is user using TASK 185
            user_COM = input(lang_expressions['port_question']).lower()
            print(user_COM)
            print(decorator_1)
            if user_COM.isnumeric() and user_COM != '0':
                # Creating string for connection to the device
                COM_string = "COM" + user_COM

                # checking ip address but need to be commented
#                 while ip_flag == False:
#                     ip_set = checking_ip_address(lang_expressions)
#                     if ip_set == True:
#                         ip_flag = True
#                 ip_flag = False

                # this command need to be deleted before releasing
                ip_set = True
                print(decorator_1)

                # Creating a list with all the possible devices
                device_list = opening_device_list()

                while device_flag and ip_set:
                    # User chooses the device, which one he wants to
                    # Completed TASK 186
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
                        # asking user if device is already booted
                        print(decorator_1)
                        print(lang_expressions['user_choice'])
                        print(f"{COM_string} ----> {user_device}")
                        print(lang_expressions['wait_prompt'])
                        print(decorator_1)

                        # returning next ip number and full name of configured device
#                         our_conf = creating_proper_configuration(user_device, 12, ip_number)
#                         actual_device = our_conf[1]
#                         ip_number = our_conf[0]
#                         our_conf = creating_proper_configuration('sssss', 2222, ip_number)

                        # connection set
                        try:
                            ser = Serial(COM_string, COM_speed)

                            # waiting for router/switch to boot
                            user_boot_flag = checking_booting(ser)

                            # counting number of gigabit and fast ports
                            device_ports = checking_switch_ports(ser)

                            # checking if device is really the device, which was wanted by user
                            proper_device = checking_device(ser, user_device, lang_expressions)

                            #print(device_ports)

                            # getting ready to create proper_initial_configuration
                            # creating_proper_configuration(user_device, device_ports, ip_number)
                            our_conf = creating_proper_configuration(user_device, 12, ip_number)
                            actual_device = our_conf[1]
                            ip_number = our_conf[0]
                            #TODO: check in lab how script work if choosing new devices


                            if user_boot_flag and proper_device:
                                print(lang_expressions['not_configured'])
                                print(decorator_1)

                                # opening file with configuration
                                stripped_list = reading_conf_files(actual_device)

                                # opening dedicated file with configuration
                                #TODO: in the future

                                # executing commands from the list
                                for command in stripped_list:
                                    send_to_console(ser, command)

                                # closing connection
                                ser.close()
                                print(f"{lang_expressions['proper_conf']}{user_device}.")
                                print(f"{lang_expressions['close_con']}{ser.name}.")
                                print(decorator_1)

                            else:
                                print(lang_expressions['start_conf'])
                                print(lang_expressions['again_prompt'])
                                print(decorator_1)
                                # closing connection
                                ser.close()
                                print(f"{lang_expressions['close_con']}{ser.name}.")
                                print(decorator_1)
                                break
                        except:
                            print(lang_expressions['not_working'])
                            print(decorator_1)

                    elif user_device == str(0):
                        break
                    else:
                        print(lang_expressions['not_supported'])

            elif user_COM == str(0):
                break
            else:
                print(lang_expressions['not_number'])
    else:
        print(lang_expressions['not_complete'])
        running_flag = False
