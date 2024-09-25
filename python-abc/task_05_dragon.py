#!/usr/bin/python3
"""Defines a Dragon class with its swim and flying mechanics"""


class SwimMixin:
    def swim(self):
        """Method for swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    def fly(self):
        """Method for flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        """Method for roaring behavior."""
        print("The dragon roars!")
