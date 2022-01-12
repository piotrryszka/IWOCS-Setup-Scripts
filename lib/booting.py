from time import sleep
from lib.commands import send_to_console
# waiting for router/switch to boot

def checking_booting(port):
    correct_flag = False
    verifying_string = ''
    while correct_flag == False:
        verifying_string += send_to_console(port, "\r\n\r")
        sleep(10)
        if 'initial configuration' in verifying_string:
            correct_flag = True
    return correct_flag

