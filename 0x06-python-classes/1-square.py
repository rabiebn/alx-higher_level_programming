#!/usr/bin/python3
"""Square Module Docs
Author: Rabia Benmer
"""


class Square:
    """Return a Square object"""
    
    def __init__(self, size):
         """
         Initialize Square attributes.
         
         Parameters:
         size (int):The size of the Square (Private instnce attribute).
         """

        self.__size = size
