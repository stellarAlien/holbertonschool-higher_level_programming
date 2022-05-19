#!/usr/bin/python3
"""module 1-write_file.py"""


def write_file(filename="", text=""):
    """open file in write mode"""
    with open(filename, mode="w", encoding="UTF8") as f:
        return (f.write(text))
