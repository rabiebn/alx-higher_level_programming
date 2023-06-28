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
    """
    def __init__(self, size):
        """
        Initialize Square.

        Attributes:
            size (int): size of square side.
        """
        self.__size = size
