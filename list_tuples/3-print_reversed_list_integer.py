#!/usr/bin/env python3
"""Prints all intergers of a list
in reverse order
"""


def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    print("{:d}".format(my_list))
