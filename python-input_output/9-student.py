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
        self.firstName = first_name
        self.lastName = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: A dictionary containing the instance's attributes.
        """
        return self.__dict__
