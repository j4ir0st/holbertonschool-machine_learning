#!/usr/bin/env python3
""" Create Confusion """
import numpy as np


def create_confusion_matrix(labels, logits):
    """ creates a confusion matrix """
    size = len(labels[0])
    confusion = np.zeros((size, size))
    x = np.where(labels == 1)[1]
    y = np.where(logits == 1)[1]
    for i in range(len(x)):
        confusion[x[i]][y[i]] += 1
    return confusion
