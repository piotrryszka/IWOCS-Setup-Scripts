# CONFIGURATION PACKAGE with data, variables etc.

# devices possible to be ie2000
ie2000 = ['TAS-1', 'MSC-1', 'MSH-1', 'MSH-2', 'MSH-3', 'MSH-4', 'MSW-1_A', 'MSW-1_B', 'MSX-1_A','MSX-1_B',
              'MSY-1_A', 'MSY-1_B', 'MSS-1_A', 'MSS-1_B'  ]

# devices possible to be ie4010
ie4010 = ['TDS-1_A', 'TDS-1_B']

# devices possible to be ASA5525 or FPR
asa_fpr = ['SDG_A', 'SDG_B']

# devices possible to be C1111
C1111 = ['ETAS-1']

# devices possible to be IR829
Ir829 = ['TIR']

# starting ip number if there is no txt file with current ip address
ip_number = 10

# decorator for better user experience
decorator_1 = ' '

# ssh connection data, needs to be properly imported into main.py when adding arguments
username = 'walter'
password = 'mel0n98'

# IP address of tftp server -> user computer
server_ip = '172.30.100.91'

# correct order of restarting devices
device_order = ['TDS-1_A', 'TDS-1_B', 'SDG-1_A', 'SDG-1_B', 'TIR', 'ETAS-1', 'TAS-1', 'MSC-1', 'MSW-1_A', 'MSW-1_B',
                'MSX-1_A', 'MSX-1_B', 'MSY-1_A', 'MSY-1_B', 'MSS-1_A', 'MSS-1_B', 'MSH-1', 'MSH-2', 'MSH-3', 'MSH-4']

# counter for correct ordering devices in table
id_number = 1

# list of commands on devices to prepare txt files with configuration
commands_list = ['sh lldp nei', 'show tech']

# TODO: ping it or do something with it whatever
# adding ip address of hub to check ping
ip_hub = '172.30.103.4'

