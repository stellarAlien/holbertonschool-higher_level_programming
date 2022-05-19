#!/usr/bin/python3
""" Module 1-square class Square"""


class Square():
    """sets square size"""

    def __init__(self, size=0):
        self.__size = size
        if(type(size) != int):
            raise TypeError("size must be an integer")
        if(size < 0):
            raise ValueError("size must be >= 0")
    def  
