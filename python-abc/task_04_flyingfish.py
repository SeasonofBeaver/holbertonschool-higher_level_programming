#!/usr/bin/python3
"""Defines a Flying Fish class. with nultiple parent classes"""
from abc import ABC, abstractmethod


class Fish(ABC):
    """Fish class that gives the classes
    the definition of fish.
    """
    def swim(self):
        """Allows the fish to swim"""
        print("The fish is swimming")

    def habitat(self):
        """tells the fish where to live"""
        print("The fish lives in water")


class Bird(ABC):
    """Bird class that gives the classes
    the definition of Bird.
    """
    def fly(self):
        """Allows the Bird to fly"""
        print("The bird is flying")

    def habitat(self):
        """tells the Bird where to live"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    "Creates a flying fish that inherits Fish and bird class."
    def swim(self):
        """overriding the swim from fish"""
        print("The flying fish is soaring!")

    def fly(self):
        """overriding the fly from bird"""
        print("The flying fish is swimming!")

    def habitat(self):
        """overriding the habitat from fish and bird"""
        print("The flying fish lives both in water and the sky!")
