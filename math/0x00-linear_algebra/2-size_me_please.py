#!/usr/bin/env python3
""" Shape """


def matrix_shape(matrix):
    """ Return shape as list """
    count = []
    c1 = 0
    for elem in matrix:
        c1 = c1 + 1
        c2 = 0
        for el in elem:
            c2 = c2 + 1
            c3 = 0
        if type(el) != int:
            for e in el:
                c3 = c3 + 1
    count.append(c1)
    count.append(c2)
    if type(el) != int:
        count.append(c3)
    return count
