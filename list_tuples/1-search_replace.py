#!/usr/bin/env python3
"""A module containing a function
that replaces all occurrences of an
element by another in a new list
"""


def search_replace(my_list, search, replace):
    return [replace if x == search else x for x in my_list]
