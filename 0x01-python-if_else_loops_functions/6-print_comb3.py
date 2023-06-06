#!/usr/bin/python3

for d1 in range(9):
    for d2 in range(d1 + 1, 10):
        if d1 == 8 and d2 == 9:
            print(f"{d1}{d2}")
            break
        print(f"{d1}{d2}", end=", ")
