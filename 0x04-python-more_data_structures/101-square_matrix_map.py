#!/usr/bin//python3
def square_matrix_map(matrix=[]):
    if(matrix is not None):
        new = list()
    for i in matrix:
        new.append(list(map(lambda x: x**2, i)))
    return(new)
