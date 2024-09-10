#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    truthList = []
    for element in my_list:
        if element % 2 == 0:
            truthList.append(True)
        else:
            truthList.append(False)
    return truthList
