#!/usr/bin/python3
"""
0-read_file Module has 1 function:
    read_file()
"""


def read_file(filename=""):
    """
    reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (string): file name to open and print.
    """

    with open(filename, encoding='UTF-8') as a_file:
        for line in a_file:
            print(line, end='')
