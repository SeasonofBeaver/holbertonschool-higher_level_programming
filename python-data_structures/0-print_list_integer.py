#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for element in my_list:
        print("{:d}".format(my_list[element-1]))
