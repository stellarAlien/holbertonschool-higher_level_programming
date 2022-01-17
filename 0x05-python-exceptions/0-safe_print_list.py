#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    s = 0
    for i in my_list[:x]:
        try:
            print(i, end="")
            s += 1
        except ValueError:
            continue
    print()
    return(s)
