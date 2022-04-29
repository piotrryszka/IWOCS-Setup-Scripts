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
#

# reading info about version from txt file
def read_version():
    with open('ie4010_show_version.txt', 'r') as my_file:
        for line in my_file:
            # looking for actual device model and version number
            if 'Cisco IOS Software' in line:
                my_list = line.split(', ')
                for x in my_list:
                    x = x.strip()
                    x = x.split(' ')
                    # getting device model
                    if 'Software' in x and 'IOS' not in x:
                        final_device = x[0]
                        print(final_device)
                    # getting actual version number
                    if 'Version' in x and final_device == 'IE4010':
                        print(x)
                        act_version = x[-4]
                        print(act_version)
                    if 'Version' in x and final_device == 'IE2000':
                        print(x)
                        act_version = x[-1]
                        print(act_version)

read_version()