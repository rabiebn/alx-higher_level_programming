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

    def to_json(self, attrs=None):
        """
        Retreives attributes in a dict representation of a Student instance.

        Args:
            attrs (list): Attributes of the Class Student to retreive.

        Return:
            attributes 'attrs' in dict representation of a Student instance.
        """
        obj_dict = dict()
        if attrs == None:
            return self.__dict__

        for k in self.__dict__.keys():
            if k in attrs:
                obj_dict[k] = self.__dict__[k]

        return obj_dict
