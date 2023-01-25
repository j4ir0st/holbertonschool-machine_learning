#!/usr/bin/env python3
""" Input """
import tensorflow.keras as K


def build_model(nx, layers, activations, lambtha, keep_prob):
    """ builds a neural network with the Keras library """
    inp = K.Input(shape=(nx, ))
    reg = K.regularizers.L2(l2=lambtha)
    for i in range(len(layers)):
        if i == 0:
            out = K.layers.Dense(units=layers[0],
                                 activation=activations[0],
                                 kernel_regularizer=reg)(inp)
        else:
            out = K.layers.Dense(units=layers[i],
                                 activation=activations[i],
                                 kernel_regularizer=reg)(out)
        if i < len(layers) - 1:
            out = K.layers.Dropout(rate=(1 - keep_prob))(out)
    model = K.Model(inputs=inp, outputs=out)
    return model
