#!/usr/bin/env python3
""" Test """
import tensorflow.keras as K


def test_model(network, data, labels, verbose=True):
    """ tests a neural network """
    test = network.evaluate(data, labels, verbose=verbose)
    return test
