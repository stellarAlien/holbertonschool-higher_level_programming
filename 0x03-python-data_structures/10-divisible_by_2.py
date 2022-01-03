#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    vlist = []
    k = 0
    for i in my_list:
        if (i % 2 == 0):
            vlist.append(True)
            k += 1
        else:
            vlist.append(False)
            k += 1
    return(vlist)
