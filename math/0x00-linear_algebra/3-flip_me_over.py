#!/usr/bin/env python3
""" Transpose """
import numpy


def matrix_transpose(matrix):
    """ Return the transpose of a 2D matrix """
    a = numpy.array(matrix)
    tr = a.T
    return tr
