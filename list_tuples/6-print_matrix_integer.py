#!/usr/bin/env python3
"""A module containing a function
that prints a matrix of integers
"""


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for column in row:
            if column == row[-1]:
                print("{:d}".format(column), end='')
            else:
                print("{:d}".format(column), end=' ')
        print()
