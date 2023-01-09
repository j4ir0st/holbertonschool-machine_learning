#!/usr/bin/env python3
""" Forward Propagation """
import tensorflow.compat.v1 as tf


create_layer = __import__('1-create_layer').create_layer


def forward_prop(x, layer_sizes=[], activations=[]):

    # Initialize the input layer with the input data
    layer = x

    # Iterate over the layers and activations and create a fully connected lyer
    for i in range(len(layer_sizes)):
        layer = create_layer(layer, layer_sizes[i], activations[i])

    # Return the output of the final layer
    return layer
