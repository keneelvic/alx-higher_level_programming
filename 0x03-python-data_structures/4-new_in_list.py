#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    news_list = []
    if idx >= 0 or idx <= len(my_list):
        news_list = [] + my_list
        news_list[idx] = element
        return news_list
    return my_list
