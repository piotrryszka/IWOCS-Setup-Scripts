from time import sleep
from lib.commands import send_to_console
# waiting for router/switch to boot

def checking_booting(port):
    correct_flag = False
    verifying_string = ''
    counter = 0
    while correct_flag == False:
        verifying_string += send_to_console(port, "\r\n\r")
        sleep(10)
        counter += 1
        if 'initial configuration' in verifying_string:
            correct_flag = True
        # waiting 5 minutes
        elif counter > 30:
            break
    return correct_flag
