#!/usr/bin/env python3
"""A module containing a function that
computes the square value of all 
integers in a matrix
"""


def square_matrix_simple(matrix=[]):
    # iterate through the items in the matrix
    return [[x ** 2 for x in row] for row in matrix]
