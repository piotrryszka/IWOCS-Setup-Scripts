# from lib.network import ssh_con
# #from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException
# from lib.data import password, username, decorator_1
#
#
# new_host = '172.30.100.10'
# ssh_con(file='TDS-1_A_test.txt', host =new_host)

# creating list with files
from os import listdir
from os.path import isfile, join

def listing_conf(us_choice):
    onlyfiles = [f for f in listdir('../tftp-conf-files') if isfile(join('../tftp-conf-files', f))]
    if us_choice in onlyfiles:
        return True
    else:
        return False

e = test('ETAS-1')
print(e)