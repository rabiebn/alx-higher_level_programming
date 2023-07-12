#!/usr/bin/python3
"""
100-append_after Module.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing
    a specific string.
    """

    new_file = []
    with open(filename, mode='r', encoding='UTF-8') as my_file:
        file_lines = my_file.readlines()

    lines = []
    for line in file_lines:
        lines.append(line)
        if search_string in line:
            lines.append(new_string)

    with open(filename, mode='w', encoding='UTF-8') as my_file:
        my_file.writelines(lines)
