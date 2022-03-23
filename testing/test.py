# TESTING
from lib.commands import send_to_console
from serial import Serial

# TODO: ustawienie wartosci domyslnych, jezeli cos sie nie wczyta to dawanie jakies 'UNKNOWN' i uzytkownik musi srpawdzic sam
# TODO: zrobic duza funkcje z tym wszystkim zeby wszystko zwracala
# TODO; pozmieniac nazwy zmiennych bo tu syf jest

ser = Serial('COM6', 9600)
send_to_console(ser, '\n')
send_to_console(ser, '\n')
send_to_console(ser, '\n')
send_to_console(ser, 'en')

e = send_to_console(ser, 'sh license udi', 0.5)

li = list(e.split())
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
                line_read = line.split()
                our_info = line_read[2:]
                print(our_info)
                state_string = ' '.join(our_info)
                # tego my stringa wsadzic w pole STATUS
                print(state_string)
            if 'License Type:' in line:
                line_read = line.split()
                our_info = line_read[2:]
                print(our_info)
                type_string = ' '.join(our_info)
                # tego my stringa wsadzic w pole EXPIRATION
                print(type_string)
            if 'ipservices' in line:
                line_read = line.split()
                our_info = line_read[3:]
                print(our_info)
                ipservices_string = ' '.join(our_info)
                # tego my stringa wsadzic w pole STATUS
                print(ipservices_string)
        if 'lanbase' in line:
            counter =+1

