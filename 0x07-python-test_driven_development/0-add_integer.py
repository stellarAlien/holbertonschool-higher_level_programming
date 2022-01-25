#!/usr/bin/python3
"""
 Module def add_integer(a, b=98)
 adds two floats and returns an integer
 """
 def add_integer(a, b=98):
     """
     adds two flaots and returns strictly an integer
     no need to worry about overflows 
     as a google search indicated that only numpy and pan\
             das have c-style fixed precision integers
     """
     if(not isinstance(a, int) or not isinstance(a, float)):
         raise TypeError("a must be an integer")
     if(not isinstance(b, int) or not isinstance(b, float)):
         raise TypeError("b must be an integer")
     x = int(a +b)
     return x
