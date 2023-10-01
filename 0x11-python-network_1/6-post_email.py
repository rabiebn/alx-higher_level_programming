#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request to the URL
with the email as a parameter,
and displays the body of the response (decoded in utf-8).
"""

from sys import argv
import requests


if __name__ == '__main__':
    data = {'email': argv[2]}

    req = requests.post(argv[1], data=data)
    print(req.text)
