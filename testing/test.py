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
