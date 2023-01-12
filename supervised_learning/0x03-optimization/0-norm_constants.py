#!/usr/bin/env python3
""" Normalization Constants """

import numpy as np


def normalization_constants(X):
    """ calculates the normalization constants of a matrix """
    u = np.average(X, axis=0)
    s = np.std(X, axis=0)

    return u, s
