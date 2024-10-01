#!/usr/bin/python3
"""Defines a Class which reads a file."""


def read_file(filename=""):
    """reads file and prints it to stdout."""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
