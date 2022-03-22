# TESTING
from lib.commands import send_to_console
from serial import Serial

ser = Serial('COM6', 9600)
e = send_to_console(ser, 'sh license udi', 0.5)

print(e)

li = list(e.split())
# e.split('')
print(li)
udi = li[11]

# UDI
print(udi)

e = send_to_console(ser, 'sh license', 2)


with open("data.txt", "w") as text_file:
    text_file.write(e)

list_of_lists = []


with open('data.txt') as f:
    for line in f:
        data = f.read()
        print(data)



# print(data)

content_list = data.split()
print(content_list)
# li = list(e.split())
# # e.split('')
# print(li)
