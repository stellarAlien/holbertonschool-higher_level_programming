#!/usr/bin/python3
""" Module 2-square class Square """


class Square:
    """ initializes size value and verifies it"""
    def __init__(self, size=0):
        self.__size = size
        if(type(size) == str):
            raise TypeError("size must be an integer")
        if (not int(size) >= 0):
            raise ValueError("size must be >= 0")
