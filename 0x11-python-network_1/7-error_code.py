#!/usr/bin/python3
"""
sends a request to the URL and displays the body of the response (utf-8).
"""

from sys import argv
import requests

if __name__ == '__main__':
    resp = requests.get(argv[1])
    if resp.status_code >= 400:
        print("Error code: {}".format(resp.status_code))
    else:
        print(resp.text)
