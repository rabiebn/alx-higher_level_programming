#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    return list(map(lambda x: list(map(lambda i: x[i]**2, range(len(x)))), matrix))
