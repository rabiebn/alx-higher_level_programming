#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    sum = 0

    for i in range(1, len(argv)):
            sum += int(argv[i])

    print("{}".format(sum))
