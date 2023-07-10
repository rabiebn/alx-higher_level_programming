#!/usr/bin/python3
"""
7-base_geometry Module
"""


class BaseGeometry():
    """
    BaseGeometry Class
    """
    def area(self):
        """
        Raises an Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that 'value' is an int > 0.

        Args:
            name (string): variable's name.
            value (int): value to be validated
        """
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
