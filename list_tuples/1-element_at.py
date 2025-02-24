#!/usr/bin/env python3
"""A module containing a function
that retrieves an element from
a list
"""
def element_at(my_list, idx):
    if idx < 0 and idx > len(my_list):
        return None
    else:
        return my_list[idx]
