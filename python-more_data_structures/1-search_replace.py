#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newList = []
    for i in my_list:
        if i == search:
            newList.append(replace)
        else:
            newList.append(i)
    return newList
