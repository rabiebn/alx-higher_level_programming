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

    def update(self, *args, **kwargs):
        """Update attributes"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if "id" in kwargs.keys():
                self.id = kwargs["id"]
            if "size" in kwargs.keys():
                self.size = kwargs["size"]
            if "x" in kwargs.keys():
                self.x = kwargs["x"]
            if "y" in kwargs.keys():
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Returns the dictionnary representation of a Square object"""
        d = super().to_dictionary()
        d["size"] = self.size
        del d["width"]
        del d["height"]

        return d
