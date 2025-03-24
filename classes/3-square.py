#!/usr/bin/env python3
"""This is a module that
contains a class square
that defines a square
"""

class Square:
    """defines a square by size"""
    def __init__(self, size=0):
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2
