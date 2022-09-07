#!/usr/bin/env python3
""" concatenates two arrays """


def cat_arrays(arr1, arr2):
    """ concatenates two arrays """
    cat = []
    for a1 in arr1:
        cat.append(a1)
    for a2 in arr2:
        cat.append(a2)
    return cat


def mat_mul(mat1, mat2):
    """ matrix multiplication """
    mul = []
    aux = []
    if len(mat1) != len(mat2[0]):
        return None
    for i in len(mat1):
        for j in len(mat2[0]):
            aux.append(mat1[i][j] * mat2[0][0])
