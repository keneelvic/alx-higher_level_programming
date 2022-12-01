#!/usr/bin/python3
def remove_char_at(str, n):
    new_String = ""
    for count, letter in enumerate(str):
        if (count != n):
            new_String += letter
    return (new_String)
