#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if(idx < 0 or idx > len(my_list)i - 1):
        return(None)
    my_list[idx - 1] = element
    return(0)
