#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with a given letter.
"""

import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    letter_data = {"q": letter}

    response = requests.post("http://0.0.0.0:5000/search_user", data=letter_data)
    try:
        user_data = response.json()
        if user_data == {}:
            print("No result")
        else:
            print("[{}] {}".format(user_data.get("id"), user_data.get("name")))
    except ValueError:
        print("Not a valid JSON")
