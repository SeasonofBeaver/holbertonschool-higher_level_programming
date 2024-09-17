#!/usr/bin/python3
"""Defines a Class for a Square"""


class Square:
    """
    An empty class to define a square.
    For now just a placeholder here for future use.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if not isinstance(position, tuple) or len(position) != 2 or \
           not all(isinstance(num, int) and num >= 0 for num in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        """retrieves the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """looks if value is a positive integer otherwise raises error

        Args:
            value (int): Size of the square given to size.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """get the square position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the value of position or raises error

        Args:
            value (tuple): Position of the square given to position.

        Raises:
            TypeError: If the value is not a positive integer tuple.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(numbers, int) for numbers in value) or
                not all(numbers >= 0 for numbers in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square with #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
