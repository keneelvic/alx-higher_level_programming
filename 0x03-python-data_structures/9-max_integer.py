#!/usr/bin/python3
def max_integer(my_list=[]):
    max_val = my_list[0]
    if len(my_list) > 0:
        for i in my_list[1:]:
            if i > max_val:
                max_val = i
        return max_val
    else:
        return None
