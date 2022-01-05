#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if (not my_list or (not search) or (not replace)):
        return(my_list)
    ls = list(my_list)
    for i in ls[0:len(ls) - 1]:
        if (ls[i] == search):
            ls[i] = replace
    return(ls)
