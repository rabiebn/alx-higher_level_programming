#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

argv = sys.argv
argc = len(argv) - 1
op_func = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
        }
if __name__ == '__main__':
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    if op not in op_func:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    operator = op_func[op]
    print("{} {} {} = {}".format(a, op, b, operator(a, b)))
