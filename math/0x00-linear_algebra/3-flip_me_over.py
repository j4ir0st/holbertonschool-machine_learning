#!/usr/bin/env python3
""" Transpose """


def matrix_transpose(matrix):
    """ Return the transpose of a 2D matrix """
    tr = []
    for c in range(len(matrix[0])):
        count = []
        for elem in matrix:
            count.append(elem[c])
        tr.append(count)
    return tr
