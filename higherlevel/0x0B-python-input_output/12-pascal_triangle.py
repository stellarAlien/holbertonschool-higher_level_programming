#!/usr/bin/python3
"""
Module 14-pascal_triangle
Contains function that returns int lists of pascal triangle
"""


def pascal_triangle(n):
    """
    the og pascal triangle
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    triangle = [[1]]
    for rows in range(2 ):
        print(triangle)
        triangle.append([a+b for a, b
                         in zip([0] + triangle[-1], triangle[-1] + [0])])


