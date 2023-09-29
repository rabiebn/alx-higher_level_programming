#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    finds num that's greater than both left and right
    """
    if len(list_of_integers) == 0:
        return None

    lst = list_of_integers
    a = 0
    z = len(lst) - 1

    if lst[a] > lst[a + 1]:
        return lst[a]
    if lst[a] > lst[z - 1]:
        return lst[z]
    mid = (a + z) // 2
    if lst[mid - 1] < lst[mid] and lst[mid + 1] < lst[mid]:
        return lst[mid]
    if lst[mid] < lst[mid - 1]:
        return find_peak(lst[a:mid + 1])
    elif lst[mid] < lst[mid + 1]:
        return find_peak(lst[mid:z + 1])
    else:
        return lst[a]
