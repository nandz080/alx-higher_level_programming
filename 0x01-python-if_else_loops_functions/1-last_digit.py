#!/usr/bin/python3

import random

# generate a random number between -10000 and 10000 (incl both min and max)
number = random.randint(-10000, 10000)

# get the last digit of the number
last_digit = abs(number) % 10

# print the output
print("Last digit of", number, "is", last_digit, end=" ")

if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
