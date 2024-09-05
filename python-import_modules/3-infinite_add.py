#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    argc = len(argv)
    i = 1
    sum = 0
    while i < argc:
        sum += int(argv[i])
        i += 1
    print("{}".format(sum))
