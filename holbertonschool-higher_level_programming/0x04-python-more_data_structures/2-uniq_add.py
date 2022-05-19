#!/usr/bin/python3
def uniq_add(my_list=[]):
    x = list()
    s = 0
    for i in my_list:
        if (i not in x):
            s = s + i
            x.append(i)
    return(s)
