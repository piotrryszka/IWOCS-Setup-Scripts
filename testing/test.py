#TODO:
# THREADS
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
#         print('*')
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
#
# # NEED TO FINISH THREADS AS WELL


# function to prepare which device need to be updated
# def prepare_software(lang_dict):
#     # empty list to return devices
#     update_list = []
#     # flag to be updated to leave loop
#     update_flag = True
#     while update_flag:
#         # question to user if he want to update sth
#         print(decorator_1)
#         user_update = input(lang_dict['ver_update'])
#         print(user_update)
#         print(decorator_1)
#         if user_update == '1':
#             # question which devices user wants to update
user_dev_list = list(map(str, input('wprowadz numerki').split()))
user_dev_list = list(dict.fromkeys(user_dev_list))
print(*user_dev_list, sep=', ')
# reading possible devices from version txt file
with open('../temp/version.txt') as file:
    new_list = []
    data = file.readlines()
    stripped_data = [e.strip() for e in data]
    print(stripped_data)
    for element in stripped_data:
        element = element.split(' ')
        new_list.append(element)
        print(element)
    print(stripped_data)
    print(new_list)
    for x in new_list:
        if x[0] in user_dev_list:
            print(x)
            print('essa')

#                 # reading all devices to check the device choice
#                 with open('static_files/project_names_of_devices.txt') as my_file:
#                     data_text = my_file.readlines()
#                     # stripping elements from list
#                     stripped_data_ver = [e.strip() for e in data_text]
#                     test_flag = False
#                     for element in stripped_data_ver:
#                         if element == user_up_dev:
#                             test_flag = True
#                 # checking if device is possible to update
#                 if user_up_dev in data and test_flag:
#                     data_list = data.split('\n')
#                     for element in data_list:
#                         if user_up_dev in element:
#                             data_final = element.split(' ')
#                             update_list.append(data_final)
#                             print("TEST PRINT -> PREPARING DATA TO UPDATE DEVICES")
#                 else:
#                     print(lang_dict['bad_device'])
#         else:
#             # leaving update version loop
#             update_flag = False
#     # returning list with the devices needs to be updated
#     return update_list
#
# prepare_software