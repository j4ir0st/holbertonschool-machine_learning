#!/usr/bin/env python3
""" Save and Load Weights """
import tensorflow.keras as K


def save_weights(network, filename, save_format='h5'):
    """ saves an entire model """
    K.models.save_weights(model=network,
                          filepath=filename,
                          save_format=save_format)
    return None


def load_weights(network, filename):
    """ loads an entire model """
    load_w = K.models.load_weights(filename, model=network)
    return load_w
