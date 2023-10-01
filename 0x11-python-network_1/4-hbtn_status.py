#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status """

import requests

if __name__ == '__main__':
    with requests.get('https://alx-intranet.hbtn.io/status') as resp:
        print("Body response:")
        print("\t- type: {}".format(type(resp)))
        print("\t- content: {}".format(resp.content))
