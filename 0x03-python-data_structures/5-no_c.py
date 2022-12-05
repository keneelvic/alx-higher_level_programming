#!/usr/bin/python3
def no_c(my_string):
    new_char = ''
    for letter in my_string:
        if letter != 'c' and letter != 'C':
            new_char += letter
    return new_char
