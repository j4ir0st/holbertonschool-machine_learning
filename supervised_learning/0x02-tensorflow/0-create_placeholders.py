#!/usr/bin/env python3
""" Placeholders """

def create_placeholders(nx, classes):
    """ returns two placeholders, x and y, for the neural network """
    x = tf.placeholder('float', shape=[None, nx])
    y = tf.placeholder('float', shape=[None, classes])
    return x, y
