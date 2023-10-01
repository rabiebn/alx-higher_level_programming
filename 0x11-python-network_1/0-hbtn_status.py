#!/usr/bin/python3
""" fetch https://intranet.hbtn.io/status ,  display response """

import urllib.request as req

if __name__ == '__main__':
    with req.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        body = resp.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
