#!/usr/bin/env python3
""" Precision """
import numpy as np


def precision(confusion):
    """ calculates the precision for each class in a confusion matrix """
    size = len(confusion[0])
    prec = np.zeros(size)
    for i in range(size):
        prec[i] = confusion[i][i] / np.sum(confusion[:, i])
    return prec
