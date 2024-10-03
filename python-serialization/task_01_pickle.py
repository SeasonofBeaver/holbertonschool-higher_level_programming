#!/usr/bin/python3
"""Defines a function in which you create an object."""
import pickle


class CustomObject():
    """Defines an Object with some attributes."""
    def __init__(self, name, age, is_student):
        """
        Initializes a CustomObject with attributes.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student or not.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Displays the object's attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serializes the CustomObject and saves it to the provided filename.

        Args:
            filename (str): The file to which the object will be serialized.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
                return True
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes a CustomObject from the provided filename.

        Args:
            filename (str): The file that the object will be deserialized from.
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                return obj
        except FileNotFoundError:
            return None
