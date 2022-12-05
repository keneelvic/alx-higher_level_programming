#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        if idx >= 0 and idx < len(my_list):
            news_list = [] + my_list
            news_list[idx] = element
            return news_list
    return my_list
