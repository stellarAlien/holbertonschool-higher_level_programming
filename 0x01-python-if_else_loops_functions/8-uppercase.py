#!/usr/bin/python3
def uppercase(str):

    if(str.isalpha() == 0):
        return(0)
    for i in range(0, len(str)):
        if(str[i].islower()):
            c = chr(ord(str[i]  - 32))
            str[i] = c
