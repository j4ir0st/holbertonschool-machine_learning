#!/usr/bin/env python3
"""
Creating a Neuron Class
"""
import numpy as np


class Neuron:
    """ Neuron Class: nx is the number of input features to the neuron """

    def __init__(self, nx):
        if not (isinstance(nx, int)):
            raise TypeError('nx must be an integer')
        if (nx < 1):
            raise ValueError('nx must be a positive integer')
        self.W = np.random.randn(1, nx)
        self.b = 0
        self.A = 0
