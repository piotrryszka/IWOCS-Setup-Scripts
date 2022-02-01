# imports
from lib.commands import send_to_console

# functions working on txt static_files

# opening possible devices to configure
def opening_device_list(file_name):
    with open(f'static_files/{file_name}', 'r') as file_devices:
                        lines = file_devices.read()
                        list_of_lists = lines.splitlines()
                        return list_of_lists
                        file_devices.close()

# reading commands from files (add argument to make this happen)
def reading_conf_files(file):
    with open(f'initial-configuration-files/{file}') as file:
        # getting commands from list
        content_list = file.readlines()
        stripped_list = [s.strip() for s in content_list]
        return stripped_list

# creating and reading conf files
def creating_proper_configuration(user_device, port_num, ip_add):
    with open('initial-configuration-files/cisco-switch4010') as f:
        lines = f.read()
        content_list = lines.split('\n')
        for x in content_list:
            # changing hostname
            if x == 'hostname xxx':
                our_index = content_list.index(x)
                content_list[our_index] = f'hostname {user_device}'
            # changing interface for whole range
            if x == 'interface GigabitEthernet1/1':
                int_index = content_list.index(x)
                content_list[int_index] = f'interface GigabitEthernet1/{str(port_num)}'
            # changing ip address
            if x == ' ip address x.x.x.x y.y.y.y':
                ip_index = content_list.index(x)
                content_list[ip_index] = f' ip address 172.30.100.{str(ip_add)} 255.255.255.255'
                ip_add +=1
        with open(f'initial-configuration-files/cisco-switch4010-{user_device}', 'w') as file:
            for row in content_list:
                file.write(str(row) + '\n')
        return ip_add, f'initial-configuration-files/cisco-switch4010-{user_device}'
