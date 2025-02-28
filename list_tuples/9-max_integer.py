#!/usr/bin/env python3
"""A module containing a function that finds
the biggest ineteger of a list
"""


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        max_val = my_list[0]
        for num in my_list:
            if num > max_val:
                max_val = num
        return max_val
