#!/usr/bin/python3
"""Defines a Class of Shapes"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Creates a Shape of the users choosing."""
    @abstractmethod
    def area(self):
        """the area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """the perimeter of the shape"""
        pass


class Circle(Shape):
    """Defines a Circle"""

    def __init__(self, radius):
        """
        Initializes a Circle with a given radius.

        Args:
            radius (int): the radius of the Circle.
        Raises:
            ValueError: If radius is not positive.
        """
        if radius < 0:
            raise ValueError("Radius must be a positive number")
        self.radius = radius

    def area(self):
        """Calculates and returns the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculates and returns the perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Concrete class representing a Rectangle."""

    def __init__(self, width, height):
        """
        Initializes a Rectangle with a given width and height.

        Args:
            width (int): the width of the Rectangle.
            height (int): the height of the Rectangle.
        Raises:
            ValueError: If width or height is not positive.
        """
        if width < 0:
            raise ValueError("Width must be a positive number")
        if height < 0:
            raise ValueError("Height must be a positive number")
        self.width = width
        self.height = height

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of the given shape.

    Args:
        shape (Shape): An instance of a class that inherits from Shape.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
