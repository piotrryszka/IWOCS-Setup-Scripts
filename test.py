import os
from contextlib import redirect_stdout
# from pythonping import ping
# import subprocess
# stream = os.popen('echo Returned output')
# output = stream.read()
# print(output)

# ping('www.google.com', verbose=True)
# essa = os.system('ipconfig')

import subprocess

# ZNAJDYWANIE slow w wypluwaniu z komend
import subprocess
output = str(subprocess.check_output("ipconfig", shell=True)).strip()
word = 'lokalne'
if output.find(word):
    print("mamy to")
print(output)

# TODO Polaczenie sie po COMIE i sprawdzenie z konsoli czy juz urzadzenie bylo skonifgurowane,
# TODO to juz lab bo, ale pomysl jest, porobienie folderow na pliki odpowiednio, ale to po swietach

print(type(output))