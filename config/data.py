
# CONFIGURATION PACKAGE with data, variables etc.

# devices possible to be ie2000
ie2000 = ['TAS-1', 'MSC-1', 'MSH-1', 'MSH-2', 'MSH-3', 'MSH-4', 'MSW-1_A', 'MSW-1_B', 'MSX-1_A', 'MSX-1_B',
          'MSY-1_A', 'MSY-1_B', 'MSS-1_A', 'MSS-1_B']

# devices possible to be ie4010
ie4010 = ['TDS-1_A', 'TDS-1_B']

# devices possible to be ASA5525 or FPR
asa_fpr = ['SDG_A', 'SDG_B']

# devices possible to be C1111
C1111 = ['ETAS-1']

# devices possible to be IR829
Ir829 = ['TIR-1']

# starting ip number if there is no txt file with current ip address
ip_number = 10

# decorators for better user experience
decorator_1 = ' '
decorator_2 = '................................'

# ssh connection data, needs to be properly imported into main.py when adding arguments
username = 'walter'
password = 'mel0n98'

# IP address of tftp server -> user computer
server_ip = '172.30.100.91'

# correct order of restarting devices
device_order = ['TDS-1_A', 'TDS-1_B', 'SDG-1_A', 'SDG-1_B', 'TIR-1', 'ETAS-1', 'TAS-1', 'MSC-1', 'MSW-1_A', 'MSW-1_B',
                'MSX-1_A', 'MSX-1_B', 'MSY-1_A', 'MSY-1_B', 'MSS-1_A', 'MSS-1_B', 'MSH-1', 'MSH-2', 'MSH-3', 'MSH-4']

# counter for correct ordering devices in table
id_number = 1

# list of commands on devices to prepare txt files with configuration
# commands_list = ['sh lldp nei', 'show tech']
commands_list = ['sh lldp nei', 'show run']

# adding ip address of hub to check ping
ip_hub = '172.30.103.4'

# counter of sends ICMP packets while checking LAN connection
count_ping = 1

# dictionary full with ip addresses of project configs devices
# dict_ip = {'TDS-1_A': '172.30.100.101', 'TDS-1_B': '172.30.100.201', 'MSC-1': '172.30.100.31', 'MSH-1': '172.30.100.41',
#            'MSH-4': '172.30.100.41', 'MSH-2': '172.30.100.42', 'MSH-3': '172.30.100.43', 'MSW-1_A': '172.30.100.103',
#            'MSW-1_B': '172.30.100.203', 'MSX-1_A': '172.30.100.105', 'MSX-1_B': '172.30.100.205', 'MSS-1_A': '172.30.100.107',
#            'MSS-1_B': '172.30.100.207', 'MSY-1_A': '172.30.100.108', 'MSY-1_B': '172.30.100.208', 'TIR-1': '172.30.103.4',
#            'ETAS-1': '172.30.102.4', 'TAS-1': '172.30.101.4', 'SDG-1_A': '172.30.100.1', 'SDG-1_B': '172.30.100.2'}

# TODO: TESTS
dict_ip = {'TDS-1_A': '192.168.182.1', 'TDS-1_B': '192.168.1.1'}

# sleep time -> break between sending ping
sleep_time = 3

# finish time -> when sending ping should end to not send packets all the time
finish_time = 10
