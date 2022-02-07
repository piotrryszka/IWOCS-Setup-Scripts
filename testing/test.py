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

from lib.network import ssh_con
#from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException
#from lib.data import password, username, decorator_1


new_host = '172.30.100.10'
ssh_con(file='TDS-1_A_test.txt', host =new_host)