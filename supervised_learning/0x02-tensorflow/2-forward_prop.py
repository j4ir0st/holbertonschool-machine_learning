#!/usr/bin/env python3
""" Forward Propagation """
import tensorflow.compat.v1 as tf


create_layer = __import__('1-create_layer').create_layer


def forward_prop(x, layer_sizes=[], activations=[]):
    """ forward propagation function """
    layer = x

    for i in range(len(layer_sizes)):
        layer = create_layer(layer, layer_sizes[i], activations[i])

    return layer
