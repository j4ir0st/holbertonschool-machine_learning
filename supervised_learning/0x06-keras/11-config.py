#!/usr/bin/env python3
""" Save and Load Configuration """
import tensorflow.keras as K


def save_config(network, filename):
    """ saves a model’s configuration in JSON format """
    json_conf = network.to_json()
    with open(filename, 'w') as f:
        j.write(json_conf)
    return None


def load_config(filename):
    """ loads a model with a specific configuration """
    load_w = K.models.model_from_json(filename)
    return load_w
