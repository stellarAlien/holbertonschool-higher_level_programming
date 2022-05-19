#!/usr/bin/python3
"""open file in append mode"""


def append_write(filename="", text=""):
    """open with append mode"""
    with open(filename, mode="a", encoding="UTF8") as f:
        return f.write(text)
