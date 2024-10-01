#!/usr/bin/python3
"""Defines a Class which turns an Object to Json."""


def class_to_json(obj):
    """returns the dictionary for JSON serialization of an object"""
    return obj.__dict__
