#!/usr/bin/python3
"""
Module 1-square
Defines class Square with private attribute size
Author: Rabia Benmer
"""


class Square:
    """
    Class Square definition

    Args:
        size (int): size of a square side

    Functions:
        __init__(self, size=0)
        size(self)
        size(self, value)
    """
    def __init__(self, size=0):
        """
        Initialize Square.

        Attributes:
            size (int): size of square side.
        """
        self.size = size
    
    @property
    def size(self):
        """
        Getter

        Return: size
        """
        return self.__size


    @setter.size
    def size(self, value):
        """
        Setter

        Args:
            value: sets size to value (if int and >= 0)
        """
        if not type(value) is int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Compute Square Area

        Return:
            area
        """
        return self.__size ** 2
