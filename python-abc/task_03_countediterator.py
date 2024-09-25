#!/usr/bin/python3
"""Defines a counted Iterator."""
from abc import ABC, abstractmethod


class CountedIterator(ABC):
    def __init__(self, some_iterable):
        """
        Initializes the class with an iterator from the provided iterable.
        Also initializes a counter keeping track of how many items are iterated

        Args:
            iterable (iterable): Any iterable object like a list,
            tuple, or string.
        """
        self.iterator = iter(some_iterable)
        self.counter = 0

    def get_count(self):
        """Returns the aleady counted elements through the iteration"""
        return self.counter

    def __next__(self):
        """with every iteration of iter the counter will be updated"""
        try:
            item = next(self.ome_iterable)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration
