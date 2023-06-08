#!/usr/bin/python3
import sys
argc_0 = "arguments."
argc_1 = "argument:"
argc_n = "arguments:"

if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv)

    if argc == 1:
        print("{} {}".format((argc - 1), argc_0))
    else:
        if argc == 2:
            print("{} {}".format((argc - 1), argc_1))
        else:
            print("{} {}".format((argc - 1), argc_n))
        for i in range(1, argc):
            print("{}: {}".format(i, argv[i]))
