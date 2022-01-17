#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        x = fct(*args)
        return (x)
    except (ZeroDivisionError, IndexError, ValueError, TypeError) as e:
        print("Exception: {}".foramt(e), file=sys.stderr)
        return None
