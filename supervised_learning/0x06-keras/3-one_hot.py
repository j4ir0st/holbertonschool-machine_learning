#!/usr/bin/env python3
""" One Hot """
import tensorflow.keras as K


def one_hot(labels, classes=None):
    """ converts a label vector into a one-hot matrix """
    size = len(labels)
    cat = K.utils.to_categorical(labels)
    return cat
