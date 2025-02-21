#!/usr/bin/env python3
""" A module that imports functions
from a file, does some maths and prints the result
"""
# import the module and the respective functions
from calculator_1 import add, sub, mul, div

# declare the variables
a = 10
b = 5

# delare the operations
add = a + b
sub = a - b
mul = a * b
div = a / b

# print to the stdout
print("{} + {} = {}".format(a, b, add))
print("{} - {} = {}".format(a, b, sub))
print("{} * {} = {}".format(a, b, mul))
print("{} / {} = {}".format(a, b, div))
