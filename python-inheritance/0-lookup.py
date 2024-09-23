#!/usr/bin/python3
"""defines an object lookup function that returns a list"""


def lookup(obj):
    """returns the list of available attributes and methods of an object"""
    return (dir(obj))