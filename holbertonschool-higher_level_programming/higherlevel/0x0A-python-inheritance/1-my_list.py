#!/usr/bin/python3
"""
Module 1-my_list.py
sort a list
"""


class MyList(list):
    """class that inherits from list"""

    def print_sorted(self):
        """prints list on ints in sorted in ascending order"""
        print(sorted(self))
