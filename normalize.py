from constants import TRANSLATION, CYRILLIC_SYMBOLS, CYRILLIC_SYMBOLS_UPPER
from string import ascii_letters, digits


def normalize(file_name):
    file_name = file_name.rsplit(".", 1)
    correct_file_name = ""
    for letter in file_name[0]:
        if letter in ascii_letters or letter in digits:
            correct_file_name += letter
        elif letter in CYRILLIC_SYMBOLS:
            correct_file_name += TRANSLATION.get(ord(letter))
        elif letter in CYRILLIC_SYMBOLS_UPPER:
            correct_file_name += TRANSLATION.get(ord(letter)).upper()
        else:
            if correct_file_name:
                if correct_file_name[-1] == "_":
                    continue
            correct_file_name += "_"
    return correct_file_name + "." + file_name[1]
