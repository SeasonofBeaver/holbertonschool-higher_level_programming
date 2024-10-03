#!/usr/bin/python3
"""Defines 2 functions in which you serialize and deserialize."""
import json


def serialize_and_save_to_file(data, filename):
    """Opens a file and and dumps data into it."""
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Reads from a file."""
    with open(filename) as f:
        json.load(f)
