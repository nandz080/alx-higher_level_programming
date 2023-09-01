#!/usr/bin/python3
""" python script that fetches https://alx-intranet.hbtn.io/status
"""

import requests

if __name__ == '__main__':
    fetched_url = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(fetched_url.text)))
    print("\t- content: {}".format(fetched_url.text))
