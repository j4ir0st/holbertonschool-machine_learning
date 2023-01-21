#!/usr/bin/env python3
""" Sensitivity """
import numpy as np


def sensitivity(confusion):
    """ calculates the sensitivity for each class in a confusion matrix """
    size = len(confusion[0])
    sens = np.zeros(size)
    for i in range(size):
        sens[i] = confusion[i][i] / confusion[i].sum()
    return sens
