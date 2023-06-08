#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv)

    print("{} argument".format((argc - 1)), end="")

    if argc == 1:
        print(".")
    else:
        for i in range(1, argc):
            if i == 1:
                print(":")
            else:
                print("s:")
            print("{}: {}".format(i, argv[i]))
