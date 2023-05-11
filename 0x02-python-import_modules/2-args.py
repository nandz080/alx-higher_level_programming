#!/usr/bin/python3
from sys import argv

if len(argv) == 1:
    print("0 arguments.")
else:
    arguments = argv[1:]
    count = len(arguments)
    print("{} argument{}:".format(count, 's' if count != 1 else ''))
    for i, arg in enumerate(arguments):
        print("{}: {}".format(i+1, arg))
