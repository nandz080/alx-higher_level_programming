#!/usr/bin/python3

output = ""
for i in range(10):
    for j in range(i, 10):
        if i != j:
            combination = "{:d}{:d}".format(i, j)
            if combination != "10":
                output += combination + ", "

output = output[:-2]  # Remove the last ", " from the string

print("{}".format(output))
