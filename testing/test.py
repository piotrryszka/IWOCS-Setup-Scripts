from serial import Serial
from lib.commands import send_to_console
from prettytable import PrettyTable
import os

ser = Serial('COM4', 9600)

output = send_to_console(ser, 'sh version', 2)
# print(output)
# print('\n')

with open('info.txt', 'w') as file:
    file.write(output)

with open('info.txt', 'r') as my_file:
    for line in my_file:
        # looking for actual software version
        if 'Version' in line:
            my_list = line.split(',')
            for x in my_list:
                if 'Version' in x:
                    x = x.strip()
                    x = x.split(' ')
                    # printing version
                    print("ACTUAL VERSION")
                    act_version = x[-1]
                    print(act_version)
        # looking for actual device model
        if 'System image file' in line:
            my_list = line.split(' ')
            for x in my_list:
                if 'flash' in x:
                    x = x.split('/')
                    x = x[1].split('-')
                    # printing device model
                    final_device = x[0]
                    print('DEVICE MODEL')
                    print(final_device)
                    print('\n')

# TODO: dodac try itp
# reading possible
# change it later, beacuse path would be different
files = os.listdir('../firmware/ie4010')
# przyporzadkowanie pierwszego argumentu pliku
file = files[0]



# PRETTY TABLE MOMENT
x = PrettyTable()
x.field_names = ["ID", "Name", "Model", "Current Version", "New Version"]
x.add_row(['1', "TDS-1_A", f"{final_device}", f'{act_version}', f'{file}'])
print(x)

# writing table to txt file
with open('table_version.txt', 'w') as file:
    file.write(str(x))
