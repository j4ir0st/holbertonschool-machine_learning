#!/usr/bin/env python3
""" Save and Load Weights """
import tensorflow.keras as K


def save_weights(network, filename, save_format='h5'):
    """ saves an entire model """
    network.save_weights(filepath=filename, save_format=save_format)
    return None


def load_weights(network, filename):
    """ loads an entire model """
    load_w = network.load_weights(filename)
    return load_w
