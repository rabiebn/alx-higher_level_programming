#!/usr/bin/python3
def uppercase(str):
    uStr = ""

    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            uStr += chr(ord(str[i]) - 32)
            continue
        uStr += str[i]

    print(uStr)
