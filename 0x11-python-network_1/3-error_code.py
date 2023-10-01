#!/usr/bin/python3
"""
sends a request to the URL and displays the body of the response (utf-8).
"""

from sys import argv
import urllib.request
import urllib.error

if __name__ == '__main__':
    try:
        with urllib.request.urlopen(argv[1]) as resp:
            print(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
