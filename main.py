# imports
from serial import Serial
from time import sleep
from lib.commands import send_to_console, checking_switch_ports, checking_ip_address
from lib.operations import opening_device_list, reading_conf_files
from lib.booting import checking_booting
from lib.languages import listing_languages, reading_language

# Program flags:
running_flag = True  # main flag, running program
system_flag = True  # flag about type of system
COM_flag = True  # flag checking COM
device_flag = True  # flag checking device
user_boot_flag = True
ip_flag = False
proper_language = True

# FIXED Variables:
COM_speed = 9600

# decorators
# some simple tricks for better user experience
decorator_1 = '|<----------------------------------------------------------------------------------------------------->|'


# main project
while running_flag:

    # choosing language
    # it has to be in english
    while proper_language:
        print("Available languages are presented below:")
        languages = listing_languages()
        print(*languages, sep = ', ')
        user_language = input("Please choose one of possible languages: ").lower()
        if user_language in languages:
            proper_language = False
            # making a list dictionary with expressions in chosen language
            lang_expressions = reading_language(user_language)
        else:
            print("You have provided wrong language, try again...")
        print(decorator_1)

    print(lang_expressions['information_prompt'])
    print(decorator_1)
    # question about complete system or one module TASK 184
    user_system = input("It is your system a complete one or it is just one module? "
                        "\nType 'Yes' if system complete, if not write anything else: ").lower()
    print(decorator_1)
    if user_system == 'yes':
        while COM_flag:
            # question about which COM port is user using TASK 185
            user_COM = input("Which COM port are you using?"
                             "\nType number of your COM port: ").lower()
            print(decorator_1)
            if user_COM.isnumeric() and user_COM != '0':
                # Creating string for connection to the device
                COM_string = "COM" + user_COM

                # checking ip address but need to be commented
#                 while ip_flag == False:
#                     ip_set = checking_ip_address()
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
                        user_device = input("Which device do you want to connect? ").upper()
                        user_list = []
                        for dev in device_list:
                            if user_device in dev:
                                user_list.append(dev)
                        print(decorator_1)
                        print("Your list of possible devices to configure: ")
                        print(*user_list, sep=', ')
                        print(decorator_1)
                        if user_device in user_list:
                            choosing_device = False

                    # Checking if the device is in the list of devices
                    if user_device in device_list:
                        # asking user if device is already booted
                        print(decorator_1)
                        print(f"Connecting to {user_device} by {COM_string}...")
                        print("Please wait patiently...")
                        print(decorator_1)

                        # connection set
                        try:
                            ser = Serial(COM_string, COM_speed)

                            # waiting for router/switch to boot
                            user_boot_flag = checking_booting(ser)

                            # counting number of gigabit and fast ports
                            device_ports = checking_switch_ports(ser)

                            #print(device_ports)

                            if user_boot_flag:
                                print("Your device has not been configured yet. What do you want to do with it?")
                                print(decorator_1)

                                # opening file with configuration
                                stripped_list = reading_conf_files()

                                # opening dedicated file with configuration
                                #TODO: in the future

                                # executing commands from the list
                                for command in stripped_list:
                                    send_to_console(ser, command)

                                # closing connection
                                ser.close()
                                print(f"Your device {user_device} has been configured properly.")
                                print(f"Connection to {ser.name} closed.")
                                print(decorator_1)

                            else:
                                print('Sorry your device has some starting configuration, we could not help you...')
                                print('If you want you can try again to connect to your device.')
                                print(decorator_1)
                                # closing connection
                                ser.close()
                                print(f"Connection to {ser.name} closed.")
                                print(decorator_1)
                                break
                        except:
                            print("Sorry, you have provided bad info. Check your ports and device.")
                            print("Probably your port is used by different process... ")
                            print("Maybe turn off the Putty client!")
                            print(decorator_1)

                    elif user_device == str(0):
                        break
                    else:
                        print("Sorry, your device is not supported by this program. Try again.")

            elif user_COM == str(0):
                break
            else:
                print("It is not number. Please try again.")
    else:
        print("It is not a complete system, I am sorry, I can't help you.")
        running_flag = False
