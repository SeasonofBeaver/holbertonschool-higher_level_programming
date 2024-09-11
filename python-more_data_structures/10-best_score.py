#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return (None)
    biggest = 0
    bigKey = None
    for keys, values in a_dictionary.items():
        if values > biggest:
            biggest = values
            bigKey = keys
    return bigKey
