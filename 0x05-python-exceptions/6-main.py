#!/usr/bin/python3
raise_exception_msg = __import__('6-raise_exception_msg').raise_exception_msg

try:
    raise_exception_msg("Yay wrong name MAFAKA")
except NameError as ne:
    print(ne)
