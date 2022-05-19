#!/usr/bin/python3
def best_score(a_dictionary):
    if(a_dictionary):
        m = max(a_dictionary, key=lambda k: a_dictionary[k])
        return(m)
    return(None)
