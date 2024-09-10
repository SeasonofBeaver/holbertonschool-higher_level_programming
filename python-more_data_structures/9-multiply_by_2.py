#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDictionary = {}
    for keys, values in a_dictionary.items():
        newDictionary[keys] = values * 2
    return newDictionary
