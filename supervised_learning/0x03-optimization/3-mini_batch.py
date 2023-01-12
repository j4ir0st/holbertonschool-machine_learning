#!/usr/bin/env python3
""" Mini-Batch """

import numpy as np
import tensorflow as tf


def train_mini_batch(X_train, Y_train, X_valid, Y_valid, batch_size=32, epochs=5, load_path="/tmp/model.ckpt", save_path="/tmp/model.ckpt"):
    """ trains a loaded neural network model using minibatch gradient descent """
    # import meta graph and restore session
    saver = tf.train.import_meta_graph(load_path + '.meta')
    sess = tf.Session()
    saver.restore(sess, load_path)

    # get tensors and ops from graph
    graph = tf.get_default_graph()
    x = graph.get_tensor_by_name("x:0")
    y = graph.get_tensor_by_name("y:0")
    accuracy = graph.get_tensor_by_name("accuracy:0")
    loss = graph.get_tensor_by_name("loss:0")
    train_op = graph.get_operation_by_name("train_op")

    # loop over epochs
    for epoch in range(epochs):
        print(f'After {epoch} epochs:')
        # shuffle data
        X_shuffle, Y_shuffle = shuffle_data(X_train, Y_train)
        # loop over batches
        for i in range(0, len(X_shuffle), batch_size):
            X_batch = X_shuffle[i:i + batch_size]
            Y_batch = Y_shuffle[i:i + batch_size]
            step = i // batch_size
            if step % 100 == 0:
                step_cost, step_accuracy = sess.run([loss, accuracy], feed_dict={x: X_batch, y: Y_batch})
                print(f'\tStep {step_number}:\n\t\tCost: {step_cost}\n\t\tAccuracy: {step_accuracy}')
            sess.run(train_op, feed_dict={x: X_batch, y: Y_batch})
        # print training cost and accuracy
        train_cost, train_accuracy = sess.run([loss, accuracy], feed_dict={x: X_train, y: Y_train})
        print(f'\tTraining Cost: {train_cost}\n\tTraining Accuracy: {train_accuracy}')
        # print validation cost and accuracy
        valid_cost, valid_accuracy = sess.run([loss, accuracy], feed_dict={x: X_valid, y: Y_valid})
        print(f'\tValidation Cost: {valid_cost}\n\tValidation Accuracy: {valid_accuracy}')
    # save session
    save_path = saver.save(sess, save_path)
    return save_path
