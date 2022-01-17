language_dictionary = {'en': {'information_prompt': '"IMPORTANT ISSUE!!!\nIf you want to leave any part of the program type 0 [zero] in your input!"',
          'dadasdsadsadasdasd': 'sdadadad'},
                        'no': {'information_prompt': 'Something in Norwegian language'},
                       }
def listing_languages():
    language_list = []
    for key in language_dictionary:
        language_list.append(key)
    return language_list

def reading_language(user_lang):
    return language_dictionary[user_lang]
