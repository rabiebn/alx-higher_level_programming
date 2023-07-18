#!/usr/bin/python3
"""Base Module"""


import json
import csv


class Base():
    """
    Base Class.

    Class Attributes:
        __nb_objects (private int)
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        init.

        Args:
            id (int).

        """
        Base.__nb_objects += 1
        if id is not None:
            self.id = id
        else:
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of 'list_objs' to a file"""

        with open("{}.json".format(cls.__name__), "w",
                  encoding='UTF-8') as file:
            if list_objs:
                file.write(cls.to_json_string(
                    list(d.to_dictionary() for d in list_objs)))
            else:
                file.write("[]")

    @staticmethod
    def from_json_string(json_string):
        """Returns list of the JSON string representation 'json_string'"""
        if json_string:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
        else:
            obj = cls(1)
        obj.update(**dictionary)

        return obj

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        try:
            file = open("{}.json".format(cls.__name__), "r", encoding='UTF-8')
        except Exception as e:
            return []

        obj_list = []
        instances = cls.from_json_string(file.read())
        for i in instances:
            obj_list.append(cls.create(**i))

        return obj_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes from CSV"""
        with open("{}.csv".format(cls.__name__), "w", newline='',
                  encoding='UTF-8') as file:
            w = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    w.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                else:
                    w.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes from CSV"""
        objs = list()
        with open("{}.csv".format(cls.__name__),
                  "r", newline='', encoding='UTF-8') as file:
            reader = csv.reader(file)
            for line in reader:
                if cls.__name__ == "Rectangle":
                    dict = {"id": int(line[0]),
                            "width": int(line[1]),
                            "height": int(line[2]),
                            "x": int(line[3]),
                            "y": int(line[4])}
                else:
                    dict = {"id": int(line[0]),
                            "size": int(line[1]),
                            "x": int(line[2]),
                            "y": int(line[3])}
                objs.append(cls.create(**dict))
        return objs
