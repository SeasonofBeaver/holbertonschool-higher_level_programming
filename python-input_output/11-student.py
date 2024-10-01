#!/usr/bin/python3
"""Defines a Class of a Student."""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: A dictionary containing the instance's attributes.
        """
        if attrs is None:
            return self.__dict__
        return {k: v for k, v in self.__dict__.items() if k in attrs}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with
        those in the provided dictionary.

        Args:
            json (dict): A dictionary containing attribute
            names and values to update the instance.
        """
        for key, value in json.items():
            setattr(self, key, value)
