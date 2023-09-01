#!/usr/bin/python3
"""python script that takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter, and finally displays
the body of the response.
"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    email_data = {'email': email}

    post_response = requests.post(url, email_data)
    print(post_response.text)
