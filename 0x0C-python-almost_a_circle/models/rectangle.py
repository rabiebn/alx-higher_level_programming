#!/usr/bin/python3
"""Module has class Rectangle"""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle Class; Inherits from class Base
    Inherited Attributes:
        id
    Class Attributes:
        __width
        __height
        __x
        __y
    Methods:
        __init__(self, width, height, x=0, y=0, id=None)
        update(self, *args, **kwargs)
        width(self)      width(self, value)
        height(self)     height(self, value)
        x(self)          x(self, value)
        y(self)          y(self, value)
        area(self)       display(self)
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
        return self.width * self.height

    def display(self):
        """Display the Rectangle with #"""
        for x in range(self.y):
            print("")
        for j in range(self.height):
            for i in range(self.width + self.x - 1):
                if i < self.x:
                    print(" ", end="")
                else:
                    print("#", end='')
            print("#")

    def __str__(self):
        """str"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute.

        Args:
            *args: tupil arguments.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Returns the dictionnary representation of a Rectangle object"""
        d = dict()
        d["id"] = self.id
        d["width"] = self.width
        d["height"] = self.height
        d["x"] = self.x
        d["y"] = self.y
        return d
