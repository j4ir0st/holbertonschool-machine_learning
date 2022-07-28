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
