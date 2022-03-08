#!/usr/bin/python3
"""module 0-read_file.py"""


def read_file(filename=""):
    """Open file"""
    with open(filename, encoding="UTF8") as f:
        print(f.read(), end="")
