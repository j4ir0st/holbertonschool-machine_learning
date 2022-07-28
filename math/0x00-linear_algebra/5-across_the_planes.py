#!/usr/bin/env python3
""" adds two matrices element-wise """


def add_arrays(arr1, arr2):
    """ adds two arrays element-wise """
    add = []
    if len(arr1) == len(arr2):
        for c in range(len(arr1)):
            count = arr1[c] + arr2[c]
            add.append(count)
        return add
    return None


def add_matrices2D(mat1, mat2):
    """ adds two matrices element-wise """
    add = []
    if len(mat1) == len(mat2):
        for c in range(len(mat1)):
            count = add_arrays(mat1[c], mat2[c])
            add.append(count)
            if count is None:
                return None
        return add
