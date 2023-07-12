#!/usr/bin/python3
"""
8-rectangle Module
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
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
