#!/usr/bin/python3

def uppercase(string):
    output = ""
    for char in string:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            char = chr(ord(char) - 32)
        output += char
    print("{}".format(output))
