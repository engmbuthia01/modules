#!/usr/bin/env python3
"""A module containing a function that
replaces an element in a list at a specific
position without modifying the original list
"""
def new_in_list(my_list, idx, element):
    my_list[idx] = element
    new_list = my_list.copy()

    if idx < 0 and idx > len(my_list):
        return new_list
    else:
        return my_list

