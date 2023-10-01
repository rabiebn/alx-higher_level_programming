#!/usr/bin/python3
"""
given letter as param, POST to http://0.0.0.0:5000/search_user
"""

from sys import argv
import requests

if __name__ == '__main__':
    if len(argv) < 2:
        letter = ""
    else:
        letter = argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q': letter}
    resp = requests.post(url, data=payload)
    try:
        resp_dict = resp.json()
        if resp_dict:
            print("[{}] {}".format(resp_dict.get('id'), resp_dict.get('name')))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
