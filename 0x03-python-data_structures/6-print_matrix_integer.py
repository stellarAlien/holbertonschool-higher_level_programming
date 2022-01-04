#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return matrix
    for i in matrix:
        le = len(i)
        k = 0
        for j in i:
            if (k == le - 1):
                print("{:d}".format(j), end="")
            else:
                print("{:d}".format(j), end=" ")
                k += 1
        print()
