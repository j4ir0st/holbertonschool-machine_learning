#!/usr/bin/env python3
""" Shape """


def matrix_shape(matrix):
    """ Return shape as list """
    count = []
    for elem in matrix:
        c1 = len(matrix)
        for el in elem:
            c2 = len(elem)
        if type(el) != int:
            for e in el:
                c3 = len(el)
    count.append(c1)
    count.append(c2)
    if type(el) != int:
        count.append(c3)
    return count
