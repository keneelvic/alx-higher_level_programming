#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [] + my_list
    return [i if i != search else replace for i in new_list]
