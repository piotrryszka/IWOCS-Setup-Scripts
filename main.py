# imports
import serial
from serial import Serial
from time import sleep

# Program flags:
running_flag = True  # main flag, running program
system_flag = True  # flag about type of system
COM_flag = True  # flag checking COM
device_flag = True  # flag checking device

# Variables:
COM_speed = 9600


# functions
# sending commands to device console
def send_to_console(ser_fun: serial.Serial, command: str, wait_time: float = 0.5):
    command_to_send = command + "\r\n"
    ser_fun.write(command_to_send.encode('utf-8'))
    sleep(wait_time)
    return ser_fun.read(ser_fun.inWaiting()).decode('utf-8')


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
                             "\nType number of your COM: ").lower()
            print(decorator_1)
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
                        print("Please wait patiently...")
                        print(decorator_1)
                        # TODO: Connect to Serial Port, Check in LAB on default router
                        # TODO: Verify from test.py options on router/switch
                        # connection set
                        try:
                            ser = Serial(COM_string, COM_speed)

                            checking_string = ''
                            # some commands to check the effect

                            # waiting for router/switch to boot
                            # avarage time to boot switch/router some device
                            sleep(1)
                            send_to_console(ser, "\r\n\r")
                            checking_string += send_to_console(ser, "\r\n\r\n")

                            if 'initial configuration' in checking_string:
                                print("Your device has not been configured yet. What do you want to do with it?")
                                print(decorator_1)
                                # tutaj dalsza kontynuacja wgrywania configu czy czegos tam jeszcze

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


                            # some basic commands
                        # testowa_lista.append(send_to_console(ser, "\nenable"))
                        # testowa_lista.append(send_to_console(ser, "sh run", wait_time=10))
                        # for i in range(1, 10):
                        #     send_to_console(ser, " ")
                        # testowa_lista.append(send_to_console(ser, "\n"))
                        # print(testowa_lista)
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
