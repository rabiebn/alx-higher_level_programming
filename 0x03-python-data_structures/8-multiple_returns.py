#!/usr/bin/python3

def multiple_returns(sentence):
    my_list = [len(sentence)]
    if sentence:
        my_list.append(sentence[0])
    else:
        my_list.append(None)

    return tuple(my_list)
