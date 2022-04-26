# CHECKING BOOTING OF NETWORK DEVICE

# imports
from time import sleep

from lib.commands import send_to_console

# waiting for router/switch to boot
def checking_booting(port):
    correct_flag = False
    verifying_string = ''
    counter = 0
    while not correct_flag:
        verifying_string += send_to_console(port, "\r\n\r")
        sleep(3)
        counter += 1
        # printing dots to make sure that script is still working
        print('.', end='')
        if 'initial configuration' in verifying_string:
            correct_flag = True
        # waiting 5 minutes
        elif counter > 100:
            break
    return correct_flag


