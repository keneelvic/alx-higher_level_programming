#!/usr/bin/python3
for num in range(0, 100):
    lnum = num % 10
    fnum = num // 10
    if num < 99:
        print("{:d}{:d},".format(fnum, lnum), end=" ")
    else:
        print("{:d}{:d}".format(fnum, lnum))
