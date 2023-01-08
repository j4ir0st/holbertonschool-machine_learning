#!/usr/bin/env python3
""" Layers """
import tensorflow.compat.v1 as tf


def create_layer(prev, n, activation):
    """ Create Layers """
    weights = tf.keras.initializers.VarianceScaling(mode='fan_avg')
    layers = tf.keras.layers.Dense(units=n,
                             activation=activation,
                             kernel_initializer=weights,
                             name='layer')
    return layers(inputs=prev)
