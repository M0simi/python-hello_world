#!/usr/bin/python3
"""a class that defines a square by based on 1-square.py"""


class Square:
    """class that have instantiation with optional"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
