#!/usr/bin/env python3
""" Train """
import tensorflow.keras as K


def train_model(network,
                data,
                labels,
                batch_size,
                epochs,
                verbose=True,
                shuffle=False):
    """ trains a model using mini-batch gradient descent """
    net = network.fit(x=data,
                      y=labels,
                      batch_size=batch_size,
                      epochs=epochs,
                      verbose=verbose,
                      shuffle=shuffle)
    return net
