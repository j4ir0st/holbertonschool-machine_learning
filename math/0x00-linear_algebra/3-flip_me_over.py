#!/usr/bin/env python3
""" Transpose """
import numpy


def matrix_transpose(matrix):
    """ Return the transpose of a 2D matrix """
    a = numpy.array(matrix).T
    tr = []
    for elem in a:
        sub = []
        for e in elem:
            sub.append(e)
        tr.append(sub)
    return tr
