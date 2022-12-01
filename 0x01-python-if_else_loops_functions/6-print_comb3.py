#!/usr/bin/python3
for fnum in range(0, 10):
    for lnum in range(fnum+1, 10):
        if fnum == 8 and lnum == 9:
            print("{:d}{:d}".format(fnum, lnum))
        else:
            print("{:d}{:d},".format(fnum, lnum), end=" ")
