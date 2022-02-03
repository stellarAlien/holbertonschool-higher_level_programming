#!/usr/bin/python3
""" Module 4-square class Square """


class Square:
    """ initializes size value and verifies it"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self, value):
        if(type(value) != int):
            raise TypeError("size must be an integer")
        if (not int(size) >= 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def size(self):
        """returns size"""
        return self.__size

    def area(self):
        """ returns square area"""

        return(self.__size**2)
