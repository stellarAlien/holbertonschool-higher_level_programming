#!/usr/bin/python3
def no_c(my_string):
    resstr = ''.join\
        ([my_string[i] for i in range(len(my_string))
         if(my_string[i] != 'C' and my_string[i] != 'c')])
    return(resstr)
