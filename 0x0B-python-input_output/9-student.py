#!/usr/bin/python3
"""
Student Module.
"""


class Student():
    """
    Student class.
    """

    def __init__(self, first_name, last_name, age):
        """
        init Student instance.

        Args:
            first_name (string): first name.
            last_name (string): last name.
            age (int): Age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retreives a dict representation of a Student instance.

        Return:
            self.__dict__
        """
        return self.__dict__
