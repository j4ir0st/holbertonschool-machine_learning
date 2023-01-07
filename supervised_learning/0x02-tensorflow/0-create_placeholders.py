#!/usr/bin/env python3
""" Placeholders """
import tensorflow.compat.v1 as tf


def create_placeholders(nx, classes):
    """ returns two placeholders, x and y, for the neural network """
    x = tf.placeholder(name="x", dtype=tf.float32, shape=(None, nx))
    y = tf.placeholder(name="y", dtype=tf.float32, shape=(None, classes))
    return x, y
