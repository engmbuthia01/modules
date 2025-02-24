#!/usr/bin/env python3
"""A module containing a function that replaces
an element of a list  at a specific position
"""


def replace_in_list(my_list, idx, element):
    if idx < 0 and idx > len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
