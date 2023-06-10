#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1:
        print("")
    else:
        for i in matrix:
            for j in range(len(i)):
                if j == len(i) - 1:
                    print("{}".format(i[len(i) - 1]))
                else:
                    print("{}".format(i[j]), end=" ")
