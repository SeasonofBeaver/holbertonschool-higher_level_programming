#!/usr/bin/python3
"""Prints out the input strings one after another."""


def say_my_name(first_name, last_name=""):
    """Prints the string that was input.

    Raises:
        TypeError: If first or last name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
