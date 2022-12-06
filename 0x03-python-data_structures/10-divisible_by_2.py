#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    seclist = [a % 2 == 0 for a in my_list]
    return seclist
