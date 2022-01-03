#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    vlist = []
    k = 0
    for i in my_list:
        if (i % 2 == 0):
            vlist[k++] = True
            print("{:d} is divisible by 2".format(i))
        else:
            print("{:d} is not  divisible by 2".format(i))
            vlist[k++] = False
    return(vlist)
