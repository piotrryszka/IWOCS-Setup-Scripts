# import paramiko
#
# def test():
#     host = "172.30.100.10"
#     port = 22
#     username = "walter"
#     # needs to be hashed
#     password = "mel0n98"
#
#     # project-config settings
#     # username = walter
#     # password = mel0n98
#     # host = f'172.30.100.{ip_number}'
#
#
#     # creating list of commands to be executed
#     #try:
#     with open("../tftp-conf-files/commands.txt", 'r') as my_file:
#         content = my_file.read()
#         content_list = content.split("\n")
#
#     # creating connection
#     ssh = paramiko.SSHClient()
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     ssh.connect(host, port, username, password)
#
#     # executing commands
#     for command in content_list:
#         stdin, stdout, stderr = ssh.exec_command(command)
#         lines = stdout.readlines()
#         print(lines)
#
#     # closing connection
#     ssh.close()
#     #except:
#     print("something went wrong")
#
# test()

# DOCUMENTATION
# https://ktbyers.github.io/netmiko/docs/netmiko/index.html


#
# from netmiko import ConnectHandler
#
# # this import is not important right now
# from getpass import getpass
#
# password = '098azerty@MS'
# username = 'msztaba'
# host = "pluton.kt.agh.edu.pl"
# device_type = 'linux'
#
#
# def try_netmiko(dev, hos, user, pas):
#     cisco1 = {
#         # autodetect is very useful in network devices
#         "device_type": f"autodetect",
#         "host": f"{host}",
#         "username": f"{user}",
#         "password": f'{pas}',
#     }
#
#     # Show command that we execute.
#     commands_list = ['ls', 'pwd', 'mkdir tescik', 'ls' ,'rmdir tescik']
#
#     # executing commands for network device
#     with ConnectHandler(**cisco1) as net_connect:
#         for command in commands_list:
#             # sending command
#             output = net_connect.send_command(command)
#             # printing output of command with error handling too
#             print(output)
#
#
#
# # executing function
# try_netmiko(device_type, host, username, password)

# from lib.network import ssh_con
# #from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException
# #from lib.data import password, username, decorator_1
#
#
# new_host = 'pluton.kt.agh.edu.pl'
# ssh_con(file='commands.txt', host =new_host)

# import tftpy
#
# server = tftpy.TftpServer('../tftpboot')
#
# server.listen('0.0.0.0', 69)
# server.stop()
# print('s')
# client = tftpy.TftpClient('tftp.digitaltorque.ca', 69)
# client.download('remote_filename', 'local_filename')
#
# import paramiko
# import time
# from getpass import getpass
# import datetime
#
# TNOW = datetime.datetime.now().replace(microsecond=0)
#
# username = 'admin'
# password = 'admin'
# scp_pass = getpass( prompt = 'Enter SCP server Password :')
#
# DEVICE_LIST = open ('09_devices')
# for RTR in DEVICE_LIST:
#     RTR = RTR.strip()
#     print ('\n #### Connecting to the device ' + RTR + '####\n' )
#     SESSION = paramiko.SSHClient()
#     SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     SESSION.connect(RTR,port=22,
#                     username=username,
#                     password=password,
#                     look_for_keys=False,
#                     allow_agent=False)
#
#     DEVICE_ACCESS = SESSION.invoke_shell()
#     DEVICE_ACCESS.send('copy nvram:startup-config scp://user@10.10.10.100//data/05_PYTHON_DEMO/ROUTER_' + RTR + '\n\n\n\n')
#     time.sleep(5)
#     DEVICE_ACCESS.send(scp_pass +'\n')
#     time.sleep(1)
#     print ('Backup completed for the device ' + RTR + '\n\n')
#
#     SESSION.close
# from netmiko import ConnectHandler
#
# # enter the IP for your TFTP server here
# TFTP_SERVER = "172.30.100.91"
#
# # to add a device, define its connection details below, then add its name
# # to the list of "my_devices"
# device1 = {
#     'device_type': 'cisco_ios',
#     'host': '10.1.1.1',
#     'username': 'admin',
#     'password': 'cisco123',
#     'secret': 'cisco123',
# }
#
# device2 = {
#     'device_type': 'cisco_xr',
#     'host': '10.1.1.2',
#     'username': 'admin',
#     'password': 'cisco123',
#     'secret': 'cisco123',
# }
#
# # make sure you add every device above to this list
# my_devices = [device1, device2]
#
# # This is where the action happens. Connect, backup, respond to prompts
# # Feel free to change the date on the backup file name below,
# # everything else should stay the same
# i = 0
# for device in my_devices:
#     i += 1
#     name = f"device{str(i)}"
#     net_connect = ConnectHandler(**device)
#     net_connect.enable()
#     copy_command = f"copy start tftp://{TFTP_SERVER}/{name}-backup-02-26-2020"
#
#     output = net_connect.send_command_timing(copy_command)
#     if "Address or name" in output:
#         output += net_connect.send_command_timing("\n")
#     if "Destination filename" in output:
#         output += net_connect.send_command_timing("\n")
#     net_connect.disconnect
#     print(output)

import subprocess
import os

def check_tftp():
    # command in cmd
    working_flag = False
    output_netstat = str(subprocess.check_output("netstat -na | findstr /R ^UDP", shell=True)).strip()
    print(output_ipconfig)
    # string to be found
    check_string = 'UDP    0.0.0.0:69'
    if check_string in output_ipconfig:
        print('TFTP server is already running...')
        working_flag = True
    else:
        print("Everything is fine, now you can turn on your TFTP SERVER...")
        working_flag = False
    return working_flag