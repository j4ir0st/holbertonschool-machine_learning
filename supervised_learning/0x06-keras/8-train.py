#!/usr/bin/env python3
""" Save Only the Best """
import tensorflow.keras as K


def train_model(network,
                data,
                labels,
                batch_size,
                epochs,
                validation_data=None,
                early_stopping=False,
                patience=0,
                learning_rate_decay=False,
                alpha=0.1,
                decay_rate=1,
                save_best=False,
                filepath=None,
                verbose=True,
                shuffle=False):
    """ trains a model using mini-batch gradient descent """
    callbacks = []
    if validation_data and early_stopping:
        early = K.callbacks.EarlyStopping(patience=patience)
        callbacks.append(early)
    if validation_data and learning_rate_decay:
        def sched(epoch):
            return alpha / (1 + decay_rate * epoch)
        lr_fn = K.callbacks.LearningRateScheduler(schedule=sched, verbose=1)
        callbacks.append(lr_fn)
    save = K.callbacks.ModelCheckpoint(filepath, save_best_only=True)
    callbacks.append(save)
    net = network.fit(x=data,
                      y=labels,
                      batch_size=batch_size,
                      epochs=epochs,
                      validation_data=validation_data,
                      callbacks=callbacks,
                      verbose=verbose,
                      shuffle=shuffle)
    return net
