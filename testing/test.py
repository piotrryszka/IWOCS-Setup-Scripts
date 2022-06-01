# from netmiko import ConnectHandler
#
# count_ping = 1
# finish_time = 30
# username ='walter'
# password = 'mel0n98'
#
# def download_license_ssh(host):
#     """
#
#     :param host: initial ip address
#     :return: NULL
#     """
#     # creating timestamp
#     # now = datetime.now()
#     # dateTimeObj = datetime.now()
#     # dateObj = dateTimeObj.date()
#     # dateStr = dateObj.strftime("%d.%m.%Y")
#     # configuration of network device
#     cisco1 = {
#         "device_type": f"cisco_ios",
#         "host": f"{host}",
#         # enabling waiting for the output much longer
#         "fast_cli": False,
#         "username": f"{username}",
#         "password": f'{password}'
#     }
#     # crating empty strings
#     state_string = ''
#     type_string = ''
#     ipservices_string = ''
#     # try:
#         # sending two commands to go into privilege mode
#     with ConnectHandler(**cisco1) as net_connect:
#         command_output = net_connect.send_command_expect('\n', cmd_verify=False)
#         command_output = net_connect.send_command_expect('en', cmd_verify=False)
#     # except:
#     #     pass
#
#     # try and except to not fail during the script and arguments
#
#     # sending command to get UDI
# # try:
#     with ConnectHandler(**cisco1) as net_connect:
#         e = net_connect.send_command_expect('sh license udi', cmd_verify=False)
#     li = list(e.split())
#     print(li)
#     # udi data
#     udi = li[-1]
#     print(udi)
# # except:
#     udi = "UNKNOWN"
#
#     # checking license and its status
#     try:
#         with ConnectHandler(**cisco1) as net_connect:
#             e = net_connect.send_command_expect('sh license', cmd_verify=False)
#             print(e)
#         # creating temporary txt file
#         with open("../temp/license_console.txt", "w") as text_file:
#             text_file.write(e)
#
#         # reading temporary txt file
#         with open('../temp/license_console.txt', 'r') as f:
#             counter = 0
#             counter_ie2000 = 0
#             lines = f.readlines()
#             for line in lines:
#                 if 'IE-4010' in udi:
#                     if counter < 1:
#                         if 'License State:' in line:
#                             line_read = line.split()
#                             our_info = line_read[2:]
#                             state_string = ' '.join(our_info)
#                         if 'License Type:' in line:
#                             line_read = line.split()
#                             our_info = line_read[2:]
#                             type_string = ' '.join(our_info)
#                         if 'ipservices' in line:
#                             line_read = line.split()
#                             our_info = line_read[3:]
#                             ipservices_string = ' '.join(our_info)
#                 if 'IE-2000' in udi:
#                     if 'iplite' in line:
#                         counter_ie2000 = 0
#                     if counter_ie2000 == 0:
#                         if 'License Type:' in line:
#                             line_read = line.split()
#                             our_info = line_read[2:]
#                             type_string = ' '.join(our_info)
#                         if 'License State:' in line:
#                             line_read = line.split()
#                             our_info = line_read[2:]
#                             state_string = ' '.join(our_info)
#                         if 'iplite' in line:
#                             line_read = line.split()
#                             our_info = line_read[3:]
#                             ipservices_string = ' '.join(our_info)
#                     if 'mrp-manager' in line:
#                         counter_ie2000 += 1
#                 if 'lanbase' in line:
#                     counter =+ 1
#     except:
#         state_string = 'UNKNOWN'
#         type_string = 'UNKNOWN'
#         ipservices_string = 'UNKNOWN'
#
#     # returning 4 strings to be used in license table
#     print(udi, state_string, type_string, ipservices_string)
#     return udi, state_string, type_string, ipservices_string
#
# download_license_ssh('172.30.100.10')

udi = 'IE-4010'

with open('../temp/license_console.txt', 'r') as f:
    counter = 0
    counter_ie2000 = 0
    lines = f.readlines()
    for line in lines:
        if 'IE-4010' in udi:
            if counter < 1:
                if 'License State:' in line:
                    line_read = line.split()
                    our_info = line_read[2:]
                    state_string = ' '.join(our_info)
                if 'License Type:' in line:
                    line_read = line.split()
                    our_info = line_read[2:]
                    type_string = ' '.join(our_info)
                if 'ipservices' in line:
                    line_read = line.split()
                    our_info = line_read[3:]
                    ipservices_string = ' '.join(our_info)
        if 'IE-2000' in udi:
            if 'iplite' in line:
                counter_ie2000 = 0
            if counter_ie2000 == 0:
                if 'License Type:' in line:
                    line_read = line.split()
                    our_info = line_read[2:]
                    type_string = ' '.join(our_info)
                if 'License State:' in line:
                    line_read = line.split()
                    our_info = line_read[2:]
                    state_string = ' '.join(our_info)
                if 'iplite' in line:
                    line_read = line.split()
                    our_info = line_read[3:]
                    ipservices_string = ' '.join(our_info)
            if 'mrp-manager' in line:
                counter_ie2000 += 1
        if 'lanbase' in line:
            counter = + 1

# state_string = 'UNKNOWN'
# type_string = 'UNKNOWN'
# ipservices_string = 'UNKNOWN'

# returning 4 strings to be used in license table
print( state_string, type_string, ipservices_string)