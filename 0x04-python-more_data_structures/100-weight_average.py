#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum_weight = 0
    sXw = 0
    for s, w in my_list:
        sum_weight += w
        sXw += s * w

    return sXw / sum_weight
