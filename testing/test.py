from serial import Serial
from lib.commands import send_to_console

ser = Serial('COM4', 9600)


output = send_to_console(ser, 'sh version', 2)
print(output)
print('\n')

with open('info.txt', 'w') as file:
    file.write(output)

with open('info.txt', 'r') as my_file:
    for line in my_file:
        if 'Version' in line:
            my_list = line.split(',')
            for x in my_list:
                if 'Version' in x:
                    x = x.strip()
                    x = x.split(' ')
                    # printing version
                    print("ACTUAL VERSION")
                    print(x[-1])



#     lines = my_file.readlines()
#     print(lines)