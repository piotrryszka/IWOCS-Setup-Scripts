import os
from contextlib import redirect_stdout
# from pythonping import ping
# import subprocess
# stream = os.popen('echo Returned output')
# output = stream.read()
# print(output)

# ping('www.google.com', verbose=True)
# essa = os.system('ipconfig')

import subprocess

# # ZNAJDYWANIE slow w wypluwaniu z komend
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

import serial
from time import sleep


def send_to_console(ser: serial.Serial, command: str, wait_time: float = 0.5):
    command_to_send = command + "\r"
    ser.write(command_to_send.encode('utf-8'))
    sleep(wait_time)
    print(ser.read(ser.inWaiting()).decode('utf-8'), end="")


with serial.Serial("COM5", timeout=1) as ser:
    print(f"Connecting to {ser.name}...")
    send_to_console(ser, "\n")
    send_to_console(ser, "\nenable")
    send_to_console(ser, "sh run", wait_time=10)
    for i in range(1, 10):
        send_to_console(ser, " ")
    send_to_console(ser, "\n")
    print(f"Connection to {ser.name} closed.")