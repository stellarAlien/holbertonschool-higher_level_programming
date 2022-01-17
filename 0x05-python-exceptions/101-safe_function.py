#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    x = 0
    try:
        return(fct(*args))
    except (RuntimeError, ValueError, TypeError, IndexError) as e:
        print("Exception: ", re, file=sys.stderr)
        return None
