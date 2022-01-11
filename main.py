# imports
from serial import Serial
from time import sleep
from lib.commands import send_to_console
from lib.operations import opening_device_list, reading_conf_files
from lib.booting import checking_booting

# Program flags:
running_flag = True  # main flag, running program
system_flag = True  # flag about type of system
COM_flag = True  # flag checking COM
device_flag = True  # flag checking device

# Variables:
COM_speed = 9600

# decorators
# some simple tricks for better user experience
decorator_1 = '----------------------------------------------------------------------'


# main project
while running_flag:
    print(decorator_1)
    print("IMPORTANT ISSUE!!!\n"
          "If you want to leave any part of the program type break in your input!")
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
            if user_COM.isnumeric():
                # Creating string for connection to the device
                COM_string = "COM" + user_COM

                # Creating a list with all the possible devices
                device_list = opening_device_list()

                while device_flag:
                    # Printing the possible devices
                    print(*device_list, sep=', ')

                    # User chooses the device, which one he wants to
                    # Completed TASK 186
                    user_device = input("Which device do you want to connect? ")
                    print(decorator_1)

                    # Checking if the device is in the list of devices
                    if user_device in device_list:
                        # asking user if device is already booted
                        # poprawic to na 0 i 1
                        user_boot_time = input("Is your device already booted or has started booting now?"
                                               "\nType 'booted' if it is ready, type whatever you want if not. ").lower()
                        print(decorator_1)
                        print(f"Connecting to {user_device} by {COM_string}...")
                        print("Please wait patiently...")
                        print(decorator_1)
                        # connection set
                        try:
                            # to tez metoda
                            ser = Serial(COM_string, COM_speed)

                            checking_string = ''
                            # some commands to check the effect

                            # waiting for router/switch to boot
                            checking_booting(user_boot_time)

                            send_to_console(ser, "\r\n\r")
                            checking_string += send_to_console(ser, "\r\n\r\n")

                            if 'initial configuration' in checking_string:
                                print("Your device has not been configured yet. What do you want to do with it?")
                                print(decorator_1)

                                # opening file with configuration
                                stripped_list = reading_conf_files()

                                # opening dedicated file with configuration

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
                                break
                        except:
                            print("Sorry, you have provided bad info. Check your ports and device.")
                            print("Probably your port is used by different process... ")
                            print(decorator_1)

                    elif user_device == "break":
                        break
                    else:
                        print("Sorry, your device is not supported by this program. Try again.")

            elif user_COM == "break":
                break
            else:
                print("It is not number. Please try again.")
    else:
        print("It is not a complete system, I am sorry, I can't help you.")
        running_flag = False
