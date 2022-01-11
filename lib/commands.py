# functions
from serial import Serial
from time import sleep

# sending commands to console
def send_to_console(ser_fun: Serial, command: str, wait_time: float = 0.5):
    command_to_send = command + "\r\n"
    ser_fun.write(command_to_send.encode('utf-8'))
    sleep(wait_time)
    return ser_fun.read(ser_fun.inWaiting()).decode('utf-8')