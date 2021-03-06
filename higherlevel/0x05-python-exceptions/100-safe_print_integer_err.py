#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except ValueError as ve:
        print("Exception:", ve, file=sys.stderr)
        return (False)
    except TypeError as te:
        print("Exception:", te, file=sys.stderr)
        return (False)
    except UnicodeError as ue:
        print("Exception:", ue, file=sys.stderr)
