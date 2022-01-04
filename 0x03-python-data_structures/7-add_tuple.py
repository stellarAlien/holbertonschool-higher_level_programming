#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    df = tuple(map(sum, zip(tuple_a, tuple_b)))
    print(df)
