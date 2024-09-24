#!/usr/bin/python3
"""Defines a VerboseList."""


class VerboseList(list):
    """A subclass of list that prints messages on item addition or removal."""

    def append(self, item):
        """Appends an item to the list and prints a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extends the list by appending all the items from the iterable and prints a notification."""
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(list(iterable)))

    def remove(self, item):
        """Removes the first occurrence of an item from the list and prints a notification."""
        super().remove(item)
        print("Removed [{}] from the list.".format(item))

    def pop(self, index=-1):
        """Removes and returns an item at the given index, printing a notification."""
        item = super().pop(index)
        print("Popped [{}] from the list.".format(item))
        return item
