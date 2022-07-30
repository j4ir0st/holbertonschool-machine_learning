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


def cat_matrices2D(mat1, mat2, axis=0):
    """ concatenates two matrices """
    cat = []
    if axis == 0:
        cat = cat_arrays(mat1, mat2)
        return cat
    else:
        for e in range(len(mat1)):
           arr = cat_arrays(mat1[e], mat2[e])
           cat.append(arr)
    return cat
