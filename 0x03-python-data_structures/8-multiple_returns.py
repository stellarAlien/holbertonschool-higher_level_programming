#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return(None)
    t = (len(sentence), sentence[0])
    return(t)
