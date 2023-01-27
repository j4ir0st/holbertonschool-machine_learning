#!/usr/bin/env python3
""" Save and Load Configuration """
import tensorflow.keras as K


def save_config(network, filename):
    """ saves a model’s configuration in JSON format """
    json_conf = network.to_json()
    with open(filename, 'w') as f:
        f.write(json_conf)
    return None


def load_config(filename):
    """ loads a model with a specific configuration """
    with open(filename, 'r') as f:
        model = f.read()
    load_c = K.models.model_from_json(model)
    return load_w
