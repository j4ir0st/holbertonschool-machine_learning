#!/usr/bin/env python3
""" Shape """


def matrix_shape(matrix):
    """ Return shape as list """
    count = []
    while(type(matrix) is list):
        count.append(len(matrix))
        matrix = matrix[0]
    return count
