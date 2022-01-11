# functions working on txt static_files

def opening_device_list():
    with open('static_files/test.txt', 'r') as file_devices:
                        lines = file_devices.read()
                        list_of_lists = lines.splitlines()
                        return list_of_lists
                        file_devices.close()

def reading_conf_files():
    with open('conf-files/basic_conf.txt') as file:
        # getting commands from list
        content_list = file.readlines()
        stripped_list = [s.strip() for s in content_list]
        return stripped_list


