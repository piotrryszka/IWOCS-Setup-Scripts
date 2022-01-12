# functions
from serial import Serial
from time import sleep

# sending commands to console
def send_to_console(ser_fun: Serial, command: str, wait_time: float = 0.5):
    command_to_send = command + "\r\n"
    ser_fun.write(command_to_send.encode('utf-8'))
    sleep(wait_time)
    return ser_fun.read(ser_fun.inWaiting()).decode('utf-8')

# counting gigabit and fast ports in devices
def checking_switch_ports(ser_port):
    send_to_console(ser_port, 'no')
    send_to_console(ser_port, 'en')
    send_to_console(ser_port, 'term len 0')
    checking_string = ''
    checking_string += send_to_console(ser_port, 'sh run', 5)
    checking_string += send_to_console(ser_port, '\n')
    number_gigabit = checking_string.count('GigabitEthernet')
    number_fast = checking_string.count('FastEthernet')
    port_dictionary = {'Gigabit': number_gigabit,
                       'Fast': number_fast
                        }
    send_to_console(ser_port, 'term len 24')
    return port_dictionary