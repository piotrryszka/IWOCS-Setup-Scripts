# all commands in different languages
language_dictionary = {'En': {'information_prompt': '"IMPORTANT ISSUE!!!\nIf you want to leave any part of the program type 0 [zero] in your input!"',
                              'module_question': "It is your system a complete one or it is just one module? \nType '1' if system complete, if not write anything else: ",
                              'port_question': "Which COM port are you using?\nType number of your COM port: ",
                              'device_question': "Which device do you want to connect? ",
                              'listing_devices': "Your list of possible devices to configure: ",
                              'wait_prompt': "Please wait patiently...",
                              'user_choice': "You have chosen this configuration...",
                              'not_configured': "Your device has not been configured yet. What do you want to do with it?",
                              'proper_conf': 'Your device has been configured properly --->',
                              'close_con': "Closed connection to ",
                              'start_conf': 'Sorry your device has some starting configuration, we could not help you...',
                              'again_prompt': 'If you want you can try again to connect to your device.',
                              'not_working': 'Sorry, you have provided bad info. Check your ports and device.\nProbably your port is used by different process...\nMaybe turn off the Putty client!',
                              'not_supported': "Sorry, your device is not supported by this program. Try again.",
                              'not_number': "It is not number. Please try again.",
                              'not_complete': "It is not a complete system, I am sorry, I can't help you.",
                              'ip_prompt': "Please set your ip address on LAN connection to 172.30.100.91/24. Take your time...",
                              'ready_ip': "If you are ready and your ip address is set, please type in '1' in console. ",
                              'good_ip': "Your IP address has been configured properly...",
                              'again_ip': "Check once again your IP address and your port...",
                              'bad_conf_ip': "Bad info try again.",
                              'proper_device': "Device is chosen properly, let's continue...",
                              'bad_device': "You have chosen bad device, try again...",
                              'deleting_logs': "Do you want to delete all logs? If yes type '1', if not type anything else.\n",
                              'print_logs': "This is a list of all saved session logs: ",
                              'timestamp': "Creating current timestamp: ",
                              'ssh_failed': "Sorry, your SSH connection cannot be established...",
                              'ssh_established': "Connection has been established correctly ...",
                              'del_info': "You have left the script, try again...",
                              'waiting_ssh': "Waiting about 10 seconds for SSH connection to be established ...",
                              'tftp_server': "Now it is time to check TFTP Server",
                              'tftp_check': "If you are ready and TFTP Server is not running, please type in '1' in console. ",
                              'tftp_occupied': 'TFTP server is already running or socket is occupied ...',
                              'tftp_free': "Everything is fine, now you can turn on your TFTP SERVER...",
                              'tftp_start': "Your TFTP server is running now...",
                              'tftp_folder': "Please choose proper folder with configs in TFTP Server application...",
                              'tftp_ip': 'Please choose proper IP address in TFTP Server application...',
                              'tftp_ready': "If you set configuration properly and you are ready, please type in '1' in console. ",
                              'tftp_good': 'Everything was set, you can continue...',

                              },
                        'No': {'information_prompt': 'Something in Norwegian language ',
                               'module_question': 'Something in Norwegian language ',
                               'port_question': 'Something in Norwegian language ',
                               'device_question': 'Something in Norwegian language ',
                               'listing_devices': 'Something in Norwegian language ',
                               'wait_prompt': "Something in Norwegian language ",
                               'user_choice': "Something in Norwegian language ",
                               'not_configured': "Something in Norwegian language ",
                               'proper_conf': "Something in Norwegian language ",
                               'close_con': "Something in Norwegian language ",
                               'start_conf': "Something in Norwegian language ",
                               'again_prompt': "Something in Norwegian language ",
                               'not_working': "Something in Norwegian language ",
                               'not_supported': "Something in Norwegian language ",
                               'not_number': "Something in Norwegian language ",
                               'not_complete': "Something in Norwegian language ",
                               'ip_prompt': "Something in Norwegian language ",
                               'ready_ip': "Something in Norwegian language ",
                               'good_ip': "Something in Norwegian language ",
                               'again_ip': "Something in Norwegian language ",
                               'bad_conf_ip': "Something in Norwegian language ",
                               'proper_device': "Something in Norwegian language ",
                               'bad_device': "Something in Norwegian language ",
                               'deleting_logs': "Something in Norwegian language ",
                               'print_logs': "Something in Norwegian language ",
                               'timestamp': "Something in Norwegian language ",
                               'ssh_failed': "Something in Norwegian language ",
                               'ssh_established': "Something in Norwegian language ",
                               'del_info': "Something in Norwegian language ",
                               'waiting_ssh': "Something in Norwegian language ",
                               'tftp_server': "Something in Norwegian language ",
                               'tftp_check': "Something in Norwegian language ",
                               'tftp_occupied': "Something in Norwegian language ",
                               'tftp_free': "Something in Norwegian language ",
                               'tftp_start': "Something in Norwegian language ",
                               'tftp_folder': "Something in Norwegian language ",
                               'tftp_ip': "Something in Norwegian language ",
                               'tftp_ready': "Something in Norwegian language ",
                               'tftp_good': "Something in Norwegian language ",

                               },
                        'Fr': {'information_prompt': 'Something in French language ',
                               'module_question': 'Something in French language ',
                               'port_question': 'Something in French language ',
                               'device_question': 'Something in French language ',
                               'listing_devices': 'Something in French language ',
                               'wait_prompt': 'Something in French language ',
                               'user_choice': 'Something in French language ',
                               'not_configured': 'Something in French language ',
                               'proper_conf': 'Something in French language ',
                               'close_con': 'Something in French language ',
                               'start_conf': 'Something in French language ',
                               'again_prompt': 'Something in French language ',
                               'not_working': 'Something in French language ',
                               'not_supported': 'Something in French language ',
                               'not_number': 'Something in French language ',
                               'not_complete': 'Something in French language ',
                               'ip_prompt': 'Something in French language ',
                               'ready_ip': 'Something in French language ',
                               'good_ip': 'Something in French language ',
                               'again_ip': 'Something in French language ',
                               'bad_conf_ip': 'Something in French language ',
                               'proper_device': 'Something in French language ',
                               'bad_device': 'Something in French language ',
                               'deleting_logs': 'Something in French language ',
                               'print_logs': 'Something in French language ',
                               'timestamp': 'Something in French language ',
                               'ssh_failed': 'Something in French language ',
                               'ssh_established': 'Something in French language ',
                               'del_info': "Something in French language ",
                               'waiting_ssh': "Something in French language ",
                               'tftp_server': "Something in French language ",
                               'tftp_check': "Something in French language ",
                               'tftp_occupied': "Something in French language ",
                               'tftp_free': "Something in French language ",
                               'tftp_start': "Something in French language ",
                               'tftp_folder': "Something in French language ",
                               'tftp_ip': "Something in French language ",
                               'tftp_ready': "Something in French language ",
                               'tftp_good': "Something in French language ",

                       }
                       }



# devices possible to be ie2000
ie2000 = ['TAS-1', 'MSC-1', 'MSH-1', 'MSH-2', 'MSH-3', 'MSH-4', 'MSW-1_A', 'MSW-1_B', 'MSX-1_A','MSX-1_B',
              'MSY-1_A', 'MSY-1_B', 'MSS-1_A', 'MSS-1_B'  ]

# devices possible to be ie4010
ie4010 = ['TDS-1_A', 'TDS-1_B']

# devices possible to be ASA5525 or FPR
asa_fpr = ['SDG_A', 'SDG_B']

# devices possible to be C1111
C1111 = ['ETAS-1']

# devices possible to be IR829
Ir829 = ['TIR']

# starting ip number, not changeable here, we can change it in main.py
ip_number = 10

# decorator for better user experience
decorator_1 = ' '

# ssh connection data, needs to be properly imported into main.py when adding arguments
#username = 'walter'
#password = 'mel0n98'

# to check connection
username = "msztaba"
# needs to be hashed
password = "098azerty@MS"
# host for tests
# host = "pluton.kt.agh.edu.pl"