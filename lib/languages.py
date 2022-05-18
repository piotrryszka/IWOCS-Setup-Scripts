# LANGUAGES HANDLING

# imports
from config.language import language_dictionary

# listing every possible language
def listing_languages():
    """

    :return:
    """
    language_list = []
    for key in language_dictionary:
        language_list.append(key)
    return language_list

# reading commands from chosen language
def reading_language(user_lang):
    """

    :param user_lang:
    :return:
    """
    return language_dictionary[user_lang]

