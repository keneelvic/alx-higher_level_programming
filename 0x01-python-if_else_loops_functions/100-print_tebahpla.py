#!/usr/bin/python3
for letters in range(122, 96, -1):
    if letters % 2 != 0:
        letters = chr(letters - 32)
        print("{}".format(letters), end="")
    else:
        letters = chr(letters)
        print("{}".format(letters), end="")
