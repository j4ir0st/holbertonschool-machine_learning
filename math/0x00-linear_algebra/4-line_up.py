#!/usr/bin/env python3
""" adds two arrays element-wise """


def add_arrays(arr1, arr2):
    """ adds two arrays element-wise """
    add = []
    if len(arr1) == len(arr2):
        for c in range(len(arr1)):
            count = arr1[c] + arr2[c]
            add.append(count)
        return add
    return None
