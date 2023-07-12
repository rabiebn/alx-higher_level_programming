#!/usr/bin/python3
"""
9-rectangle Module
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle Class
    """

    def __init__(self, width, height):
        """
        init Rectangle.

        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Claculates Rectangle's area.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        str
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
