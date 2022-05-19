#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if (not key):
        return(a_dictionary)
    if(key in a_dictionary):
        a_dictionary.pop(key)
    return(a_dictionary)
