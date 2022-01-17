language_dictionary = {'en': {'information_prompt': '"IMPORTANT ISSUE!!!\nIf you want to leave any part of the program type 0 [zero] in your input!"',
                              'module_question': "It is your system a complete one or it is just one module? \nType '1' if system complete, if not write anything else: ",
                              'port_question': "Which COM port are you using?\nType number of your COM port: ",
                              'device_question': "Which device do you want to connect? ",
                              'listing_devices': "Your list of possible devices to configure: ",
                              },
                        'no': {'information_prompt': 'Something in Norwegian language',
                               'module_question': 'Something in Norwegian language',
                               'port_question': 'Something in Norwegian language',
                               'device_question': 'Something in Norwegian language',
                               'listing_devices': 'Something in Norwegian language',
                               }
                       }
# listing every possible language
def listing_languages():
    language_list = []
    for key in language_dictionary:
        language_list.append(key)
    return language_list

# reading commands from chosen language
def reading_language(user_lang):
    return language_dictionary[user_lang]
