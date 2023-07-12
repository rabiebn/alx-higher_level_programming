#!/usr/bin/python3
"""
100-append_after Module.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing
    a specific string.
    """

    new_file = ""
    with open(filename, mode='r', encoding='UTF-8') as my_file:
        for line in my_file:
            new_file += line
            if search_string in line:
                new_file += search_string

    with open(filename, mode='w', encoding='UTF-8') as my_file:
        my_file.writelines(lines)
