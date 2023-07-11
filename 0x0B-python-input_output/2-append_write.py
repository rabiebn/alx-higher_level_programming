#!/usr/bin/python3
"""
2-append_write Module has 1 function:
    append_write()
"""


def append_write(filename="", text=""):
    """
    append a string to a text file (UTF8),
    and returns number of characters written,
    creates file if it didn't exist.

    Args:
        filename (string): file name to append to.
        text (string): string to append to 'filename'.

    Returns:
        Number of characters appended to 'filename'.
    """

    with open(filename, mode='a', encoding='UTF-8') as a_file:
        a_file.write(text)

    return len(text)
