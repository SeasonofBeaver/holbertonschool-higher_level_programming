#!/usr/bin/python3
"""Defines a function in which you create an object."""
import pickle


class CustomObject():
    """Defines an Object with some attributes."""
    def __init__(self, name, age, is_student):
        """gets a name an age and asks if its a student."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Displays the object's attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serializes the CustomObject and saves it to the filename."""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception as e:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize the CustomObject and loads from file."""
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                return obj
        except (FileNotFoundError, pickle.UnpicklingError):
            return None
