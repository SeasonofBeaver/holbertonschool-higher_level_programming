#!/usr/bin/python3
"""Defines a Class for a Rectangle"""


class Rectangle:
    """A class that defines a Rectangle with height and width"""


    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the Rectangle.
            height (int): The height of the Rectangle.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.height = height
    
    @property
    def width(self):
        """width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """looks if value is a positive integer otherwise raises error

        Args:
            value (int): width of the Rectangle given to width.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """looks if value is a positive integer otherwise raises error

        Args:
            value (int): height of the Rectangle given to height.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
