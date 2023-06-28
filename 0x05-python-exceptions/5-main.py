#!/usr/bin/python3
raise_exception = __import__('5-raise_exception').raise_exception
try:
    raise_exception()
    print("raised from func")
except TypeError as te:
    print("Exception raised")
