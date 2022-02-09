#CHECKING BOOTING OF NETWORK DEVICE

# imports
from time import sleep
from lib.commands import send_to_console

# waiting for router/switch to boot
def checking_booting(port):
    correct_flag = False
    verifying_string = ''
    counter = 0
    while correct_flag == False:
        verifying_string += send_to_console(port, "\r\n\r")
        # to discuss how often to refresh computing vs user experience
        sleep(3)
        counter += 1
        if 'initial configuration' in verifying_string:
            correct_flag = True
        # waiting 5 minutes
        elif counter > 100:
            break
    return correct_flag

