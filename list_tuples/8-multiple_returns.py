#!/usr/bin/env python3
"""A module that returns a module with
the length of a string and its first character
"""


def multiple_returns(sentence):
    if len(sentence) == 0:
        return(0, None)
    else:
        return(len(sentence), sentence[0])
