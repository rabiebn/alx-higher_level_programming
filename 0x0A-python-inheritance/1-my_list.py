#!/usr/bin/python3
"""
1-my_list Module.
"""


class MyList(list):
    """
    MyList class subclass of 'list'.
    """

    def __init__(self):
        """
        init
        """
        super().__init__(self)

    def print_sorted(self):
        """
        Function prints a sorted list.
        """
        my_list = self[:]
        my_list.sort()
        print(my_list)
