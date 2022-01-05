#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if((not key) or (not a_dictionary) or (not value)):
        return(a_ditionary)
    if(key in a_dictionary):
        a_dictionary[key] = value
    else:
        a_dictionary.update({key: value})
    return(a_dictionary)
