#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    s = 0
    for i in my_list[0:x]:
        try:
            print("{:d}".format(i), end="")
            s += 1
        except (ValueError, TypeError, IndexError):
            pass
    print()
    return(s)
