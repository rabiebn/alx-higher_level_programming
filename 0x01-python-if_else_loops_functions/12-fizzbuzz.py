#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 or i % 5 == 0:
            if i % 3 != 0:
                print("Buzz", end=" ")
                continue
            elif i % 5 != 0:
                print("Fizz", end=" ")
                continue
            print("FizzBuzz", end=" ")
        else:
            print("{}".format(i), end=" ")
