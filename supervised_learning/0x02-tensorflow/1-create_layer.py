#!/usr/bin/env python3
""" Layers """
import tensorflow.compat.v1 as tf
import tensorflow.keras as kr


def create_layer(prev, n, activation):

    weights = kr.initializers.VarianceScaling(mode='fan_avg')
    layers = kr.layers.Dense(units=n,
                             activation=activation,
                             kernel_initializer=weights,
                             name='layer')
    return layers(inputs=prev)
