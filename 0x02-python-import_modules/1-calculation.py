#!/usr/bin/python3

if __name__ == "__main__":

	from calculator_1 import add, sub, mul, div

	# Define variables
	a = 10
	b = 5
	
	# Perform calculations
	add_result = add(a, b)
	sub_result = sub(a, b)
	mul_result = mul(a, b)
	div_result = div(a, b)

	# Print the results
	print("{} + {} = {}".format(a, b, add_result))
	print("{} - {} = {}".format(a, b, sub_result))
	print("{} * {} = {}".format(a, b, mul_result))
	print("{} / {} = {}".format(a, b, div_result))
