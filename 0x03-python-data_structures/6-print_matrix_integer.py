#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        exit(0)
    elif len(matrix) == 1 and len(matrix[0]) == 0:
        print("")
    else:
        for i in matrix:
            for j in range(len(i)):
                if j == len(i) - 1:
                    print("{:d}".format(i[len(i) - 1]))
                else:
                    print("{:d}".format(i[j]), end=" ")
