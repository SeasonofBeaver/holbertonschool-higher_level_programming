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
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the Rectangle."""
        return self.__height * self.__width

    def perimeter(self):
        """returns the perimeter of the Rectangle.
        or 0 if one length is 0
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return self.__height * 2 + self.__width * 2

    def __str__(self):
        """returns a string of # and new lines to be printed.
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        rectangle = []
        for i in range(self.__height):
            rectangle.append("#" * self.__width)
            if i != self.__height - 1:
                rectangle.append("\n")
        return "".join(rectangle)

    def __repr__(self):
        """returns a string representation of the rectangle.
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """prints a message when the class is deleted.
        """
        print("Bye rectangle...")
