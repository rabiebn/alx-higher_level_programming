#!/usr/bin/python3
"""
0-read_file Module has 1 function:
    read_file()
"""


def read_file(filename=""):
    with open(filename, mode='r', encoding='UTF-8') as a_file:
        for line in a_file:
            print(line, end='')
