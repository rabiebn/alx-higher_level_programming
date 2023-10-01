#!/usr/bin/python3
""" fetch https://intranet.hbtn.io/status ,  display response """

import urllib.request as req

if __name__ == '__main__':
    with req.urlopen('https://intranet.hbtn.io/status') as resp:
        body = resp.read()
        print("Body response:")
        print("\t- type: {}\n\t- content: {}\n\t- utf8 content: {}".format(
            type(body), body, body.decode('utf-8')))
