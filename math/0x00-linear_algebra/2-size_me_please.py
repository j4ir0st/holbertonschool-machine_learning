#!/usr/bin/env python3
""" Shape """
import numpy


def matrix_shape(matrix):
    """ Return shape as list """
    a = numpy.array(matrix, dtype=int)
    li = list(a.shape)
    return li
