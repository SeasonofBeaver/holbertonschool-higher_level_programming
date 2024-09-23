#!/usr/bin/python3
"""A class MyList which inherits the list."""

class MyList(list):
    """Inherits from the list."""

    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """Prints the list, sorted in ascending order."""
        print(sorted(self))
