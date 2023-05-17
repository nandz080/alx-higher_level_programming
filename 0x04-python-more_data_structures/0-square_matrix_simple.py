#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Use map and lambda function to square each value in the matrix
    new_matrix = list(map(lambda row: list(map(lambda num: num ** 2, row)), matrix))
    return new_matrix
