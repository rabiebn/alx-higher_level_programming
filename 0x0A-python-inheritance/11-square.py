#!/usr/bin/python3
"""
10-square Module.
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Square class.
    """

    def __init__(self, size):
        """
        init

        Args:
            size (int): integer > 0.
        """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Area of the Square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        str
        """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
