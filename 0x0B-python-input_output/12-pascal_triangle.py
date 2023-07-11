#!/usr/bin/python3
"""
12-pascal_triangle Module
"""


def pascal_triangle(n):
    """
    Constracts a Pascale Triangle of n.

    Args:
        n (int): integer.

    Return:
        list of lists of integers representing pascale's triangle.
    """

    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    p_tri = [[1]] + [[1, 1] for i in range(n - 1)]

    for i in range(n):
        if i + 1 < n:
            for j in range(i + 1):
                if j + 1 < len(p_tri[i]):
                    p_tri[i + 1].insert(j + 1, p_tri[i][j] + p_tri[i][j + 1])

    return p_tri
