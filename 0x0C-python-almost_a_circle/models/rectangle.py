#!/usr/bin/python3
"""Rectanlge Module."""


from models.base import Base


class Rectangle(Base):
    """Rectangle Class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Init

        Args:
            width (int)
            height (int)
            x (int)
            y (int)
            id (int)
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        super().__init__(id)

    @property
    def width(self):
        """width Getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """width Setter"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

    @property
    def height(self):
        """height Getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """height Setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """x Getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x Setter"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y Getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y Setter"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Calculating Area"""
        return self.__width * self.__height

    def display(self):
        """Display the Rectangle with #"""

        for j in range(self.__height):
            for i in range(self.__width - 1):
                print("#", end='')
            print("#")

    def __str__(self):
        """str"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x,  self.__y, self.__width, self.__height)
