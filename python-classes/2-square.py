#!/usr/bin/python3
"""Defines a Class for a Square"""


class Square:
    """
    An empty class to define a square.
    For now just a placeholder here for future use.
    """
    def __init__(self, size=0):
        """Creates a new square.

        Args:
            size (int): The size of the created square, initialized with 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is smaller than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
