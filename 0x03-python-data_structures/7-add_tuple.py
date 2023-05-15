#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Extract the first two elements from each tuple or use 0 if the tuple is smaller than 2
    a = tuple_a[0] if len(tuple_a) >= 1 else 0
    b = tuple_a[1] if len(tuple_a) >= 2 else 0
    c = tuple_b[0] if len(tuple_b) >= 1 else 0
    d = tuple_b[1] if len(tuple_b) >= 2 else 0

    # Perform the addition of the elements and return the result as a tuple
    return (a + c, b + d)
