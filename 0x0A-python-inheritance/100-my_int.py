#!/usr/bin/python3
"""
100-my_int Module.
"""


class MyInt(int):
    """
    MyInt rebel class child of int class.
    """

    def __eq__(self, other):
        """
        eq
        """
        return super().__ne__(self)

    def __ne__(self, other):
        """
        ne
        """
        return super().__eq__(self)
