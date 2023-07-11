#!/usr/bin/python3
"""
1-write_file Module has 1 function:
    write_file()
"""


def write_file(filename="", text=""):
    """
    write a string to a text file (UTF8),
    and returns number of characters written.

    Args:
        filename (string): file name to write to.
        text (string): string to write to 'filename'.

    Returns:
        Number of characters written to 'filename'.
    """

    with open(filename, mode='w', encoding='UTF-8') as a_file:
        a_file.write(text)

    return len(text)
