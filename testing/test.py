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
# import logging
#
# logging.basicConfig(filename='logname.txt',
#                             filemode='a',
#                             format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
#                             datefmt='%H:%M:%S',
#                             level=logging.DEBUG)
#
# logging.info("Running Urban Planning")
# logging.info("ESASASASA")

# import subprocess
# file_ = open('shell_output.txt', 'w+')
# subprocess.run('echo Hello from shell', shell=True, stdout=file_)
# file_.close()
# from lib.commands import send_to_console
#
# our_string = 'blablalb'
# number_of_ports = str(24)
# ip_address = str(10)
#
# with open('../initial-configuration-files/cisco-switch4010') as f:
#     lines = f.read()
#     print(lines)
#     content_list = lines.split('\n')
#     print(type(lines))
#     for x in content_list:
#         # changing hostname
#         if x == 'hostname xxx':
#             our_index = content_list.index(x)
#             content_list[our_index] = f'hostname {our_string}'
#         # changing interface for whole range
#         if x == 'interface GigabitEthernet1/1':
#             int_index = content_list.index(x)
#             content_list[int_index] = f'interface GigabitEthernet1/{number_of_ports}'
#         # changing ip address
#         if x == ' ip address x.x.x.x y.y.y.y':
#             ip_index = content_list.index(x)
#             content_list[ip_index] = f' ip address 172.30.100.{ip_address} 255.255.255.255'
#     with open(f'../initial-configuration-files/cisco-switch4010-{our_string}', 'w') as file:
#         for row in content_list:
#             file.write(str(row) + '\n')

# # LOGGING
# import logging
# import time
#
# aaaa = 'example output from function/string'
#
# logging.basicConfig(level = logging.INFO, filename = time.strftime("Configurationdsadas - my-%Y-%m-%d.log"))
#
# logging.info(f"> {aaaa }")







# import paramiko
# from getpass import getpass
# import time
#
# ip = raw_input("Please enter your IP address: ")
# username = raw_input("Please enter your username: ")
# password = getpass()
#
# remote_conn_pre=paramiko.SSHClient()
# remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# remote_conn_pre.connect(ip, port=22, username=username,
#                         password=password,
#                         look_for_keys=False, allow_agent=False)
#
# remote_conn = remote_conn_pre.invoke_shell()
# output = remote_conn.recv(65535)
# print output
#
# remote_conn.send("show ip int brief\n")
# time.sleep(.5)
# output = remote_conn.recv(65535)
# print output
#
# remote_conn.send("conf t\n")
# time.sleep(.5)
# output = remote_conn.recv(65535)
# print output
#
# remote_conn.send("end\n")
# time.sleep(.5)
# output = remote_conn.recv(65535)
# print output
import logging
#
# logging.basicConfig(level=logging.INFO, format='%(message)s')
# logger = logging.getLogger()
# logger.addHandler(logging.FileHandler('test.log', 'a'))
# print = logger.info
#
# print('yo!')


# moje
# import logging
# logging.basicConfig(
#      filename='rokoko.txt',
#      level=logging.INFO,
#      format= '[%(asctime)s] %(levelname)s ->>> %(message)s',
#      datefmt='%H:%M:%S'
#  )
# logger = logging.getLogger()
# print = logger.info
# print('esss')

# import logging
#
# log = logging.getLogger(__name__)
#
# def do_something():
#     log.debug("Doing something!")
#
# do_something()

# class Tee:
#     def write(self, *args, **kwargs):
#         self.out1.write(*args, **kwargs)
#         self.out2.write(*args, **kwargs)
#     def __init__(self, out1, out2):
#         self.out1 = out1
#         self.out2 = out2
#
# import sys
# sys.stdout = Tee(open("log.txt", "w"), sys.stdout)

# import readline
# readline.write_history_file('history.txt')
# print('sdasd')
# print('sd')
#
# from datetime import datetime
#
# # Current date time in local system
# print(datetime.now())
# print(datetime.date(datetime.now()))

import os

files = os.listdir('../logs')
print(files)
for file in files:
    os.remove(f'../logs/{file}')
