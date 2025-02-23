#!/usr/bin/env python3
"""This is a module
containing a function that prints
all integers of a list
"""

def print_list_integer(my_list=[]):
    for x in my_list:
        print("{:d}".format(x))
