#!/usr/bin/python3
"""Defines a Class which writes into a file."""


def write_file(filename="", text=""):
    """writes a string to a text file."""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
