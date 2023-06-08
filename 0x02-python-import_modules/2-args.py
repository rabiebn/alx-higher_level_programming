#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv)

    print("{} arguments".format((argc - 1)), end="")

    if argc == 1:
        print(".")
    else:
        print(":")
        for i in range(1, argc):
            print("{}: {}".format(i, argv[i]))
