#!/usr/bin/python3
"""
100-append_after Module.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing
    a specific string.
    """

    with open(filename, mode='r', encoding='UTF-8') as my_file:
        lines = my_file.readlines()

    for i in range(len(lines)):
        if search_string in lines[i]:
            lines.insert(i + 1, new_string)

    with open(filename, mode='w', encoding='UTF-8') as my_file:
        my_file.writelines(lines)
