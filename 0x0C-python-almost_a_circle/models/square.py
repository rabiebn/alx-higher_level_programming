#!/usr/bin/python3
"""Module has 1 class Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square Class; inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize"""
        height = width = size
        super().__init__(width, height, x, y, id)

    @property
    def size(self):
        """Size getter"""
        return self.height

    @size.setter
    def size(self, size):
        """Size Setter"""
        self.width = self.height = size

    def __str__(self):
        """Str"""
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.height)
