#!/usr/bin/python3

def padding_0(my_list):
    while len(my_list) < 2:
        my_list.append(0)
    return my_list


def add_tuple(tuple_a=(), tuple_b=()):
    my_list = []
    a = padding_0(list(tuple_a))
    b = padding_0(list(tuple_b))

    for i in range(2):
        my_list.append(a[i] + b[i])

    return tuple(my_list)
