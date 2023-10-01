#!/usr/bin/python3
"""
sends a request to the URL and displays the value of X-Request-Id in the
response header
"""

import requests
from sys import argv

if __name__ == '__main__':
    resp = requests.get(argv[1])
    print(resp.headers.get('X-Request-Id'))
