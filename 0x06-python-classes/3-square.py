#!/usr/bin/python3
"""
Module 3-square
Defines class Square with private attribute size
Author: Rabia Benmer
"""


class Square:
    """
    Class Square definition

    Args:
        size (int): size of a square side
    """
    def __init__(self, size=0):
        """
        Initialize Square.

        Attributes:
            size (int): size of square side.
        """
        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Compute Square Area"""
        return self.__size ** 2
