#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        d = dict()
        tmp = {}
        for key, value in a_dictionary.items():
            val = value * 2
            tmp = {key: val}
            d.update(tmp)
        return (d)
    return (None)
