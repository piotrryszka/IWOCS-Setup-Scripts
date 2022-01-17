# import os
# from contextlib import redirect_stdout
# from pythonping import ping
# import subprocess
# stream = os.popen('echo Returned output')
# output = stream.read()
# print(output)

# ping('www.google.com', verbose=True)
# essa = os.system('ipconfig')
#
# import subprocess

# ZNAJDYWANIE slow w wypluwaniu z komend
# import subprocess
# output = str(subprocess.check_output("ipconfig", shell=True)).strip()
# word = 'lokalne'
# if output.find(word):
#     print("mamy to")
# print(output)
#
# # TODO Polaczenie sie po COMIE i sprawdzenie z konsoli czy juz urzadzenie bylo skonifgurowane,
# # TODO to juz lab bo, ale pomysl jest, porobienie folderow na pliki odpowiednio, ale to po swietach
#
# print(type(output))

# LACZENIE SIE PO SERIALU, ale nie dziala

# import serial
#
# s = serial.Serial('COM3')
# res = s.read()
# print(res)

# import serial
# from time import sleep
#
#
# def send_to_console(ser: serial.Serial, command: str, wait_time: float = 0.5):
#     command_to_send = command + "\r"
#     ser.write(command_to_send.encode('utf-8'))
#     sleep(wait_time)
#     print(ser.read(ser.inWaiting()).decode('utf-8'), end="")
#
#
# with serial.Serial("/dev/tty.AirConsole-68-raw-serial", timeout=1) as ser:
#     print(f"Connecting to {ser.name}...")
#     send_to_console(ser, "")
#     send_to_console(ser, "enable")
#     send_to_console(ser, "show ap summary", wait_time=2)
#     print(f"Connection to {ser.name} closed.")

# import serial
# import sys
# import time
#
# import credentials
#
# READ_TIMEOUT = 8
#
#
# def main():
#
#     print("\nInitializing serial connection")
#
#     console = serial.Serial(
#         port='COM3',
#         baudrate=9600,
#         parity="N",
#         stopbits=1,
#         bytesize=8,
#         timeout=READ_TIMEOUT
#     )
#
#     if not console.isOpen():
#         sys.exit()
#
#     console.write("\r\n\r\n")
#     time.sleep(1)
#     input_data = console.read(console.inWaiting())
#     if 'Username' in input_data:
#         console.write(credentials.username + '\r\n')
#     time.sleep(1)
#     input_data = console.read(console.inWaiting())
#     if 'Password' in input_data:
#         console.write(credentials.password + '\r\n')
#     time.sleep(1)
#     input_data = console.read(console.inWaiting())
#     print(input_data)
#
#
# if __name__ == "__main__":
#     main()

# import serial
#
# ser = serial.Serial('COM3')  # open first serial port
# print(ser.portstr)       # check which port was really used
# ser.write(str.encode('allon'))     # write a string COS W BAJTACH
# ser.close()             # close port

# import serial
# from time import sleep
#
#
# from lib.commands import send_to_console
#
#
# with serial.Serial("COM5", timeout=1) as ser:
#     print(f"Connecting to {ser.name}...")
#     send_to_console(ser, "\n")
#     send_to_console(ser, "\nenable")
#     send_to_console(ser, "sh run", wait_time=10)
#     for i in range(1, 10):
#         send_to_console(ser, " ")
#     send_to_console(ser, "\n")
#     print(f"Connection to {ser.name} closed.")
#
#
# import os
#
# # Print the current working directory
# print("Current working directory: {0}".format(os.getcwd()))

# # Change the current working directory
# os.chdir('static_files')
#
# # Print the current working directory
# print("Current working directory: {0}".format(os.getcwd()))
# test_input = input("Wprowadz nazwe urzadzenia, ktore chcesz skonfigurowac:")
# with open(f'../conf-files/{test_input}.txt') as file:
#     content_list = file.readlines()
#     stripped = [s.strip() for s in content_list]
#     print(content_list)
#     print(stripped)
#
# # x_file = open('links.txt')
# lines = x_file.readlines()
# print(lines)

# trying to catch up logs from putty
# def send_to_console(ser_fun: serial.Serial, command: str, wait_time: float = 0.5):
#     command_to_send = command + "\r\n"
#     ser_fun.write(command_to_send.encode('utf-8'))
#     sleep(wait_time)
#     return ser_fun.read(ser_fun.inWaiting()).decode('utf-8')

# test_input = input("Wprowadz cos testowego: ")
# with open(f'../logs/{test_input}.txt', 'a') as file:
#     for x in range(1, 11):
#         file.write(f'ip address 192.168.1.{x}')
#         file.write('\n')
#
#     # test in lab how saving logs to files should work
#     # file.write(send_to_console())
#
# test_opening = input("Co otworzyc: ")
#
# with open(f'../logs/{test_opening}.txt', 'r') as file:
#     # cały plik sobie zczytuje
#     #data = file.read()
#
#     # caly plik zczytuje linia po linii do jednej duzej listy, problem z parsowaniem
#     data_list = file.readlines()
#     # stripowanie tej listy
#     stripped_list = [s.strip() for s in data_list]
#     print(stripped_list)

    #print(data)

# with open('../static_files/test.txt', 'r') as file_devices:
#                     lines = file_devices.read()
#                     list_of_lists = lines.splitlines()
#                     print(list_of_lists)
#                     file_devices.close()
import logging

logging.basicConfig(filename='logname.txt',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

logging.info("Running Urban Planning")
logging.info("ESASASASA")