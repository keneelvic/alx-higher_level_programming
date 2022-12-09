#!/usr/bin/python3
from functools import reduce


def roman_to_int(roman_string):
    if roman_string:
        dictionary_rom = {
                'XL': 40,
                'CD': 400,
                'IV': 4,
                'IX': 9,
                'CM': 900,
                'X': 10,
                'I': 1,
                'V': 5,
                'C': 100,
                'L': 50,
                'D': 500,
                'M': 1000,
        }
        i = 0
        num = 0
        while i < len(roman_string):
            if (i + 1 < len(roman_string) and
                    roman_string[i:i+2] in dictionary_rom):
                num += dictionary_rom[roman_string[i:i+2]]
                i += 2
            else:
                num += dictionary_rom[roman_string[i]]
                i += 1
        return num
    elif not roman_string or None:
        return 0
