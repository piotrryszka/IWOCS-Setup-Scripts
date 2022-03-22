# TESTING
from lib.commands import send_to_console
from serial import Serial

# TODO: ustawienie wartosci domyslnych, jezeli cos sie nie wczyta to dawanie jakies 'UNKNOWN' i uzytkownik musi srpawdzic sam
# TODO: zrobic duza funkcje z tym wszystkim zeby wszystko zwracala
# TODO; pozmieniac nazwy zmiennych bo tu syf jest

ser = Serial('COM6', 9600)
e = send_to_console(ser, '\n')
e = send_to_console(ser, '\n')
e = send_to_console(ser, '\n')
e = send_to_console(ser, 'en')





e = send_to_console(ser, 'sh license udi', 0.5)

print(e)

li = list(e.split())
# e.split('')
print(li)
udi = li[11]

# UDI
print(udi)

# sprawdzanie licencji oraz jej stanu
e = send_to_console(ser, 'sh license', 2)


with open("data.txt", "w") as text_file:
    text_file.write(e)

list_of_lists = []

# flags to leave script properly
flag_1 = False
flag_2 = False

with open('data.txt') as f:
    counter =0
    lines = f.readlines()
    for line in lines:
        print(line)
        if counter < 1:
            if 'License State:' in line:
                e = line.split()
                our_status = e[2:]
                print(our_status)
                my_string = ' '.join(our_status)
                # tego my stringa wsadzic w pole STATUS
                print(my_string)
                flag_1 = True
            if 'License Type:' in line:
                e = line.split()
                our_status = e[2:]
                print(our_status)
                my_string = ' '.join(our_status)
                # tego my stringa wsadzic w pole EXPIRATION
                print(my_string)

        if 'ipservices' in line:
            print("ESSA")
        if 'lanbase' in line:
            counter =+1



#         data = f.read()
#         print(data)



# print(data)

# content_list = data.split()
# print(content_list)
# li = list(e.split())
# # e.split('')
# print(li)
