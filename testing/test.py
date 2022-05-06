# #TODO:
# # THREADS
# import _thread
# import time
# import threading
#
# # Define a function for the thread
# def print_time( threadName, delay):
#    count = 0
#    while count < 5:
#       time.sleep(delay)
#       count += 1
#       print ("%s: %s" % ( threadName, time.ctime(time.time()) ))
#
# def print_star(delay):
#     while 1:
#         time.sleep(delay)
#         print('*', end='')
#
# def counting_process(delay):
#     while 1:
#         time.sleep(delay)
#         e = threading.active_count()
#         print(e)
#
#
#
# # Create threads as follows
# try:
#    _thread.start_new_thread( print_time, ("Thread-1", 1, ) )
#    _thread.start_new_thread( print_time, ("Thread-2", 1, ) )
#    _thread.start_new_thread(print_star, (0.5,))
#    _thread.start_new_thread(counting_process, (2,))
#    e = threading.active_count()
#    print(e)
#
# except:
#    print ("Error: unable to start thread")
#
#
# while 1:
#    pass
# reading temporary txt file

# udi = 'IE-4010'
#
# with open('ie2000_show_license.txt', 'r') as f:
#     counter = 0
#     lines = f.readlines()
#     for line in lines:
#         print(line)
#         print('EEEE')
#         if 'IE-4010' in udi:
#             if counter < 1:
#                 if 'License State:' in line:
#                     line_read = line.split()
#                     our_info = line_read[2:]
#                     state_string = ' '.join(our_info)
#                     # print(state_string)
#                 if 'License Type:' in line:
#                     line_read = line.split()
#                     our_info = line_read[2:]
#                     type_string = ' '.join(our_info)
#                     print(type_string)
#                 if 'ipservices' in line:
#                     line_read = line.split()
#                     our_info = line_read[3:]
#                     ipservices_string = ' '.join(our_info)
#                     # print(ipservices_string)
#         if 'IE-2000' in udi:
#             if 'License Type:' in line:
#                 line_read = line.split()
#                 our_info = line_read[2:]
#                 type_string = ' '.join(our_info)
#                 print(type_string)
#
# state_string = 'UNKNOWN'
# type_string = 'UNKNOWN'
# ipservices_string = 'UNKNOWN'

# collecting license data from device
# def download_license(ser = 'COM1'):
#     # crating empty strings
#     state_string = ''
#     type_string = ''
#     ipservices_string = ''
#
#     # try and except to not fail during the script and arguments
#
#     # sending command to get UDI
#     try:
#         udi = 'IE-2000'
#         # udi = 'IE-4010'
#     except:
#         udi = "UNKNOWN"
#
#     # checking license and its status
#     try:
#         # e = send_to_console(ser, 'sh license', 2)
#
#         # reading temporary txt file
#         with open('ie2000_show_license.txt', 'r') as f:
#         # with open('license_console.txt', 'r') as f:
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
#                         counter_ie2000 +=1
#                 if 'lanbase' in line:
#                     counter =+1
#     except:
#         state_string = 'UNKNOWN'
#         type_string = 'UNKNOWN'
#         ipservices_string = 'UNKNOWN'
#
#     # returning 4 strings to be used in license table
#     return udi, state_string, type_string, ipservices_string
#
# print(download_license())

udi = 'IE-4010-4S24P:FDO2250U0AV'
if 'IE-4010' in udi:
    print('ee')