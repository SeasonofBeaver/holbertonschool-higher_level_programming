#!/usr/bin/python3
"""Defines an Animal Class and its subclasses."""
from abc import ABC


class Animal(ABC):
    """defines an Animal."""

    @abstractmethod
    def sound(self):
        """Includes the sound of the animal"""
        pass


class Dog(Animal):
    """represents a dog in this class."""

    def sound(self):
        """Implements the sound method to return 'Bark'."""
        return "Bark"


class Cat(Animal):
    """represents a cat in this class."""

    def sound(self):
        """Implements the sound method to return 'Meow'."""
        return "Meow"
