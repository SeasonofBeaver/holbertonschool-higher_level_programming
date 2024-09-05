#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv)
    if argc == 1:
        print("0 arguments.")
    elif argc == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(argc - 1))

    for i in range(1, argc):
        print("{}: {}".format(i, argv[i]))
