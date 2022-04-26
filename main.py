# imports
import sys
from serial import Serial
from time import sleep

from lib.commands import send_to_console, checking_switch_ports, checking_ip_address, checking_device, check_tftp, \
    to_conf_mode
from lib.operations import opening_device_list, reading_conf_files, creating_proper_configuration, deleting_files, \
    deleting_conf, saving_dev, list_saved_dev, saving_license, saving_info_lic, reading_license, deleting_dev_logs, \
    deleting_dev_license, download_license, sh_version, read_version, saving_ver_table, add_ip, saving_ping_table, \
    deleting_dev_ping, deleting_dev_version, deleting_project_logs, checking_stat_lic, deleting_dev_pro_ping
from lib.booting import checking_booting
from lib.languages import listing_languages, reading_language
from lib.logging import *
from lib.network import ssh_con, ssh_download
from lib.functions import printing_logs, creating_timestamp, start_tftp, user_tftp, final_tftp, check_com, order_dev, \
    list_dev, create_table, kill_tftp, kill_putty, create_table_ver, add_row_ver, prepare_software, check_ping, \
    check_license, create_dir, ping_projects
from config.data import ip_number, decorator_1, device_order, id_number, commands_list, decorator_2, dict_ip

# Program flags:
running_flag = True  # main flag, running program
system_flag = True  # flag about type of system
com_flag = True  # flag checking COM
device_flag = True  # flag checking device
user_boot_flag = True  # flag checking if device chosen by user is booted
ip_flag = False  # flag if ip is correctly set by user
proper_language = False  # flag if the language chosen by user is possible to be used
del_flag = False  # flag to check what user want to do after deleting logs
tftp_flag = True  # flag to check if the port UDP 69 is taken
ssh_flag = True  # flag to configure devices by ssh connections
update_flag = True  # flag to check if user wants to download some new software versions

# FIXED Variables:
COM_speed = 9600  # serial port speed
dictionary_dev = {}  # empty dictionary to be later filled with proper restart order
order_dict = {}  # empty dictionary with devices model and last octet of ip number
conf_devices_list = []  # empty list later filled with already configured devices
license_dict = {}  # empty dictionary later to be filled with license linked things
update_list = []  # empty list later filled with devices to update software on them

# main project
while running_flag:
    # choosing language
    while not proper_language:
        print("Available languages are presented below:")
        languages = listing_languages()
        print(*languages, sep=', ')
        user_language = input("Please choose one of possible languages: ").title()
        print(user_language)
        if user_language in languages:
            proper_language = True
            # making a list dictionary with expressions in chosen language
            lang_expressions = reading_language(user_language)
        elif user_language == "0":
            lang_expressions = reading_language('En')
            proper_language = True
        else:
            print("You have provided wrong language, try again...")
        print(decorator_1)

    # creating_timestamp
    creating_timestamp(lang_dict=lang_expressions)
    print(decorator_1)

    # checkinf possible version of software to be downloaded
    checking_stat_lic(lang_expressions)

    # info to user how to leave any part of program
    print(lang_expressions['information_prompt'])
    print(decorator_1)

    # creating table with configuration licenses
    conf_table = create_table()
    conf_table.title = (lang_expressions['conf_lic'])

    # deleting console logs, pretty table with licenses files and device logs files
    printing_logs(lang_expressions)
    user_del = input(lang_expressions['deleting_logs'])
    del_flag = deleting_files(lang_dict=lang_expressions, user_input=user_del)
    if user_del == '1':
        # calling functions to delete support and logs files
        deleting_dev_license()
        deleting_dev_logs()
        deleting_dev_version()
        deleting_dev_ping()
        deleting_project_logs()
        deleting_dev_pro_ping()
    print(user_del)
    if del_flag:
        print(lang_expressions['del_info'])
        break
    else:
        pass
    print(decorator_1)

    # question and function about killing putty process to make COM free
    dec_putty = input(lang_expressions['putty_kill'])
    print(dec_putty)
    kill_putty(dec_putty)

    # question about complete system or one module TASK 184
    print(decorator_1)
    user_system = input(lang_expressions['module_question']).lower()
    print(user_system)
    print(decorator_1)
    if user_system == '1':
        while com_flag:
            # question about which COM port is user using TASK 185
            check_com(lang_dict=lang_expressions)
            user_COM = input(lang_expressions['port_question']).lower()
            print(user_COM)
            if user_COM.isnumeric() and user_COM != '0':

                # Creating string for connection to the device
                COM_string = "COM" + user_COM

                # Creating a list with all the possible devices
                device_list = opening_device_list(file_name='project_names_of_devices.txt')

                # listing already conf devices
                order_dict = list_saved_dev()
                print(decorator_1)

                while device_flag:
                    # User chooses the device, which one he wants to
                    choosing_device = True

                    while choosing_device == True:
                        # reading configured devices from txt file to dictionary
                        order_dict = list_saved_dev()
                        # reading full info with restart order, model and ip address to dictionary
                        dictionary_dev = order_dev(conf_devices_list, device_order, dictionary_dev, order_dict)

                        # deleting already configured devices from available devices to be chosen by the user
                        # simple handling exceptions
                        try:
                            for key in dictionary_dev:
                                conf_devices_list.append(dictionary_dev[key]['device'])
                            for x in conf_devices_list:
                                if x in device_list:
                                    device_list.remove(x)
                        except:
                            pass

                        # printing already initial configured devices
                        list_dev(device_list=conf_devices_list, lang_dict=lang_expressions)

                        # question about choosing_device by the user
                        user_device = input(lang_expressions['device_question']).upper()
                        print(user_device)
                        user_list = []

                        for dev in device_list:
                            # checking if the string provided by the user has the same beginning as possible devices to configure
                            if dev.startswith(user_device):
                                user_list.append(dev)
                        print(decorator_1)
                        print(lang_expressions['listing_devices'])
                        print(*user_list, sep=', ')
                        print(decorator_1)
                        if user_device in user_list:
                            choosing_device = False

                    # Checking if the device is in the list of devices
                    if user_device in device_list:

                        print(decorator_1)
                        print(lang_expressions['user_choice'])
                        print(f"{COM_string} ----> {user_device}")
                        print(lang_expressions['wait_prompt'])
                        print(decorator_1)

                        # TODO for tests it is commented (TRY AND EXCEPT) and networking commands
                        # TODO: move all commands one tab
                        #                         try:

                        # reading ip address from txt file
                        try:
                            with open('temp/ip_number.txt', 'r') as f:
                                new_ip = f.read()
                                ip_number = int(new_ip)
                        except:
                            pass

                        # TODO: testing needs to be uncommented

                        # setting COM connection
                        # ser = Serial(COM_string, COM_speed)

                        # waiting for router/switch to boot
                        # user_boot_flag = checking_booting(port = ser)

                        # counting number of gigabit and fast ports
                        # device_ports = checking_switch_ports(ser_port = ser)

                        # checking if device is really the device, which was wanted by user
                        # proper_device = checking_device(ser_port = ser, user_device = user_device, lang_dict = lang_expressions)

                        # returning next ip number and full name of configured device to download to specified device
                        # our_conf = creating_proper_configuration(user_device = user_device, port_num = device_ports['Gigabit'], ip_add = ip_number)
                        our_conf = creating_proper_configuration(user_device=user_device, port_num=1, ip_add=ip_number)

                        # remembering old IP number, last octet is important to save to txt file
                        ip_save = ip_number

                        # returning tuple with full name device and next iip number to bes used
                        actual_device = our_conf[1]  # name of device
                        ip_number = our_conf[0]  # new ip address incremented by +1

                        # saving ip address to txt file
                        with open('temp/ip_number.txt', 'w') as f:
                            f.write(str(ip_number))

                        # TODO: DELETE IT
                        user_boot_flag = True
                        proper_device = True

                        if user_boot_flag and proper_device:

                            print(lang_expressions['not_configured'])
                            print(decorator_1)

                            # going to configuration mode
                            # to_conf_mode(ser)

                            # opening file with configuration
                            actual_device = actual_device
                            stripped_list = reading_conf_files(file=actual_device)

                            # executing commands from the list
                            for command in stripped_list:
                                # send_to_console(ser, command)
                                # printing dots to inform user that script is still working
                                print('.', end='')

                            print(decorator_1)

                            # TODO: UNCOMMENT IT
                            # checking info about license on the device
                            # returning tuple with our data
                            # license_data = download_license(ser)
                            license_data = download_license()

                            # reading license data to variables use to fill txt file
                            udi = license_data[0]
                            state_string = license_data[1]
                            type_string = license_data[2]
                            ipservices_string = license_data[3]

                            # checking proper configuration license for IE4010
                            ok_not = check_license(udi, state_string, type_string, ipservices_string)

                            print(decorator_1)

                            # saving the name of configured device to the txt file
                            saving_dev(f'{user_device} {ip_save}')

                            # reading ID number from txt file
                            try:
                                with open('temp/id_number.txt', 'r') as f:
                                    new_id = f.read()
                                    id_number = int(new_id)
                            except:
                                pass

                            # sending command to switch with sh version
                            # sh_version(ser)

                            # saving prepared data to txt, later will be prepared table report with it
                            # TUTAJ ROBOTA
                            read_version(id_number, user_device)

                            # TESTING
                            # saving info about licenses and devices to the txt file with incremented ID counter
                            id_number = saving_info_lic(id_number, user_device, udi, ipservices_string, state_string,
                                                        type_string, ok_not)

                            # saving ID number to txt file
                            with open('temp/id_number.txt', 'w') as f:
                                f.write(str(id_number))

                            # closing connection
                            # ser.close()
                            print(f"{lang_expressions['proper_conf']}{user_device}.")
                            # print(f"{lang_expressions['close_con']}{ser.name}.")
                            print(decorator_1)
                            print('---------------------------------------------------')
                            print(decorator_1)

                            # question if user has finished initial configuration of devices
                            finish_conf = input(lang_expressions['finish_conf'])
                            print(finish_conf)
                            print(decorator_1)
                            if finish_conf == '1':
                                # exit the COM connections
                                device_flag = False
                                com_flag = False
                            else:
                                # configuring next device
                                device_flag = True

                        # TODO: needs to be uncommented
                        else:
                            print(lang_expressions['start_conf'])
                            print(lang_expressions['again_prompt'])
                            print(decorator_1)

                            # closing connection
                            # ser.close()
                            # print(f"{lang_expressions['close_con']}{ser.name}.")
                            print(decorator_1)
                            break
                            # TODO: UNCOMMENT
                        #                         except:
                        # bad chosen device or it is not working
                        print(lang_expressions['not_working'])
                        print(decorator_1)

                    elif user_device == str(0):
                        break
                    else:
                        print(lang_expressions['not_supported'])

            # leaving script by '0' input
            elif user_COM == str(0):
                break
            else:
                # bad user input about COM port
                print(lang_expressions['not_number'])
                print(decorator_1)

        # SSH CONNECTIONS
        else:

            # reading info about licenses to table
            reading_license(conf_table)

            # saving already configured devices
            date_string = saving_license(table=conf_table)

            # printing table with licenses to console
            print(conf_table)

            # printing prompt about UNKNOWN in table
            print(lang_expressions['unknown_license'])
            print(decorator_1)

            # creating pretty table with versions
            ver_table = create_table_ver(lang_expressions)

            # adding all rows from txt file to version table
            add_row_ver(ver_table)

            # saving version table to txt file
            saving_ver_table(ver_table)

            # printing version table to the console
            print(ver_table)
            print(lang_expressions['info_ver'])
            print(decorator_1)

            # checking if user want to upload new license to the device
            update_list = prepare_software(lang_expressions)

            # updating version software list with ip addresses
            update_list = add_ip(update_list)

            # not printing empty list
            if len(update_list) > 0:
                print(lang_expressions['upd_dev'])
                for x in range(0, len(update_list)):
                    print(update_list[x][1], end=', ')
                print(decorator_1)

            # updating software by tftp and LAN connections
            # TODO:
            # praca nad wgrywaniem softu po tftp do roznych urzadzen
            # tutaj bedzie tworzona ta lista, mozna przesunac pozniej, ale to przed wgrywaniem konfigu projektowego trzeba bedzie robic
            if len(update_list) > 0:
                for element in update_list:
                    # JAKIES WATKI PODODAWAC
                    print(f'Now upgrading software in {element[1]} device with this IP address {element[-1]}!')

            print(decorator_1)

            # going to ssh connections
            print(lang_expressions['ssh_move'])
            print(decorator_1)

            # TODO: UNCOMMENT CHECKING COM CONNECTION
            # checking ip address is correctly set
            # while ip_flag == False:
            #     ip_set = checking_ip_address(lang_dict = lang_expressions)
            #     if ip_set == True:
            #         ip_flag = True

            print(decorator_1)

            # reminding to user to connect LAN cables like in the configuration
            print(lang_expressions['connect_cable'])

            # killing tftp server is user forgot to do so
            kill_tftp()

            # checking if server tftp is already running
            while tftp_flag:
                tftp_flag = check_tftp(lang_dict=lang_expressions)

            # starting TFTP server
            start_tftp(lang_dict=lang_expressions)

            # user instructions to set config of TFTP Server
            user_tftp(lang_dict=lang_expressions)

            # checking if server is running
            working_tftp = final_tftp()

            # SSH connection established
            print(lang_expressions['waiting_ssh'])
            print(decorator_1)

            # checking if all devices can ping each other
            ping_table = check_ping(lang_expressions)

            # saving ping table to txt file and printing it to console
            saving_ping_table(ping_table)

            # printing information what to do if the table is not correct
            print(lang_expressions['check_ping'])

            # need to be done again to actualize the dictionary
            order_dict = list_saved_dev()
            dictionary_dev = order_dev(conf_devices_list, device_order, dictionary_dev, order_dict)
            print(decorator_1)

            # printing prompt about going to project configs
            print(lang_expressions['project_conf'])
            print(decorator_1)
            print(decorator_2)
            print(decorator_1)

            # SSH CONFIGURATION LOOP
            while ssh_flag and working_tftp:
                # testing automating of restarting devices
                # need to be reversed order to do the reload in a good way
                for k in reversed(dictionary_dev.keys()):
                    print(lang_expressions['now_device'])
                    print(f"{dictionary_dev[k]['device']} -> {dictionary_dev[k]['ip']}")
                    print(decorator_1)
                    # connection with specified by user IP address and project configuration
                    # try and except to not crash the script
                    try:
                        ssh_con(file=dictionary_dev[k]['device'], host=dictionary_dev[k]['ip'])
                    except:
                        print(lang_expressions['no_con_dev'])
                        print(f"{dictionary_dev[k]['device']} <--> {dictionary_dev[k]['ip']}")
                        print(decorator_1)
                    finally:
                        print(decorator_2)
                        print(decorator_1)
                # changing ssh_flag to False to leave the loop
                ssh_flag = False

            # check ping connection
            # loop to send commands to every ip address with configured devices
            ping_projects(lang_expressions, dictionary_dev)

            print(decorator_2)
            print(decorator_1)

            # project configs downloaded, now collecting data from devices
            print(lang_expressions['download_com'])
            print(decorator_1)
            print(decorator_2)
            print(decorator_1)

            # loop to send commands to every ip address and device
            for k in reversed(dictionary_dev.keys()):
                # creating directories for different files
                create_dir(dictionary_dev[k]['device'], lang_expressions)
                for command in commands_list:
                    print(lang_expressions['collect_data'])
                    print(
                        f"IP: {dict_ip[dictionary_dev[k]['device']]}, Device: {dictionary_dev[k]['device']}, Command: {command}")
                    print(decorator_1)
                    try:
                        ssh_download(host=dict_ip[dictionary_dev[k]['device']], device=dictionary_dev[k]['device'],
                                     command=command)
                    except:
                        print(lang_expressions['no_con_dev'])
                        print(f"{dictionary_dev[k]['device']} <--> {dict_ip[dictionary_dev[k]['device']]}")
                        print(decorator_1)
                    finally:
                        print(decorator_2)
                        print(decorator_1)

            # leaving main part of script after configuration
            running_flag = False

            # closing tftp server application
            kill_tftp()

    else:
        print(lang_expressions['not_complete'])
        running_flag = False

# LAST COMMANDS IN SCRIPT
# deleting all user-configuration files created while the script was running
print(decorator_1)
# deleting_conf(lang_dict = lang_expressions)

