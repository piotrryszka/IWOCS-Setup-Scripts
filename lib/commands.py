# functions
from serial import Serial
from time import sleep
import subprocess

#decorator
decorator_1 = '|<----------------------------------------------------------------------------------------------------->|'


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

# checking if ip address was properly set by user
def checking_ip_address():
    print("Please set your ip address on LAN connection to 172.30.100.91/24. Take your time...")
    print(decorator_1)
    user_input = input("If you are ready and your ip address is set, please type in '1' in console. ")
    print(decorator_1)
    IP_flag = False
    continue_flag = True
    while continue_flag:
        if user_input == "1":
            output_ipconfig = str(subprocess.check_output("ipconfig", shell=True)).strip()
            ip_address = '10.83.6.83'
            if ip_address in output_ipconfig:
                IP_flag = True
                print("Your IP address has been configured properly...")
            else:
                IP_flag = False
                print("Check once again your IP address and your port...")
            continue_flag = False
        else:
            print("Bad info try again")
            break
    return IP_flag