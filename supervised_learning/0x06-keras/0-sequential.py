#!/usr/bin/env python3
""" Sequential """
import tensorflow.keras as K


def build_model(nx, layers, activations, lambtha, keep_prob):
    """ builds a neural network with the Keras library """
    model = K.Sequential(name="sequential")
    reg = K.regularizers.L2(l2=lambtha)
    for i in range(len(layers)):
        if i == 0:
            model.add(K.layers.Dense(units=layers[0],
                                     activation=activations[0],
                                     kernel_regularizer=reg,
                                     input_shape=(nx, )))
        else:
            model.add(K.layers.Dense(units=layers[1],
                                     activation=activations[1],
                                     kernel_regularizer=reg))
        if i < len(layers) - 1:
            model.add(K.layers.Dropout(rate=(1 - keep_prob)))
    return model
