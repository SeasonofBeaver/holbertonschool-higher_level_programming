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
        self.__size = size

    @property
    def size(self):
        """retrieves the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """looks if value is a positive integer otherwise raises error"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
