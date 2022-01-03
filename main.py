# imports
import serial
from serial import Serial
from pprint import pprint

# Program flags:
running_flag = True  # main flag, running program
system_flag = True  # flag about type of system
COM_flag = True  # flag checking COM
device_flag = True  # flag checking device

# Variables:
COM_speed = 9600

while running_flag:
    print("IMPORTANT ISSUE!!!\n"
          "If you want to leave any part of the program type break in your input!\n")
    # question about complete system or one module TASK 184
    user_system = input("It is your system a complete one or it is just one module? "
                        "\nType 'Yes' if system complete, if not write anything else: ").lower()
    if user_system == 'yes':
        while COM_flag:
            # question about which COM port is user using TASK 185
            user_COM = input("Which COM port are you using?"
                             "\nType number of your COM: ").lower()
            if user_COM.isnumeric():
                # Creating string for connection to the device
                COM_string = "COM" + user_COM

                # Creating a list with all the possible devices
                with open('static_files/test.txt', 'r') as file_devices:
                    lines = file_devices.read()
                    list_of_lists = lines.splitlines()
                    file_devices.close()

                while device_flag:
                    # Printing the possible devices
                    print(*list_of_lists, sep=', ')

                    # User chooses the device, which one he wants to
                    # Completed TASK 186
                    user_device = input("Which device do you want to connect? ")

                    # Checking if the device is in the list of devices
                    if user_device in list_of_lists:
                        print(f"Connecting to {user_device} by {COM_string}...")

                        # TODO: Connect to Serial Port, Check in LAB on default router
                        ser_connection = Serial(COM_string, COM_speed)
                        data = ser_connection.readline(5)
                        print(data)
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