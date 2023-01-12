#!/usr/bin/env python3
""" Shuffle Data """

import numpy as np


def shuffle_data(X, Y):
    """ shuffles the data points in two matrices the same way """
    x = X[np.random.permutation(len(X))]
    np.random.seed(0)
    y = Y[np.random.permutation(len(Y))]

    return x, y
