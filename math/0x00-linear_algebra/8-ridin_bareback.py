#!/usr/bin/env python3
""" concatenates two arrays """


def mat_mul(mat1, mat2):
    """ matrix multiplication """
    mul = []
    if len(mat2) != len(mat1[0]):
        return None
    for i in range(len(mat1)):
        aux = []
        for j in range(len(mat2[0])):
            a = 0
            for k in range(len(mat2)):
                a += mat1[i][k] * mat2[k][j]
            aux.append(a)
        mul.append(aux)
    return(mul)
