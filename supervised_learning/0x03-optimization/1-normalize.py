#!/usr/bin/env python3
""" Normalize """

import numpy as np


def normalize(X, m, s):
    """ normalizes (standardizes) a matrix """
    u = [(x - m) for x in X]
    z = u / s

    return z
