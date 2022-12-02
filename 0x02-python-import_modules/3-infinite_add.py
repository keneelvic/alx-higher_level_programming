#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    i = 0
    if len(argv) == 1:
        print(int("0"))
    else:
        for eachArgs in range(1, len(argv)):
            i += int(argv[eachArgs])
        print(i)
