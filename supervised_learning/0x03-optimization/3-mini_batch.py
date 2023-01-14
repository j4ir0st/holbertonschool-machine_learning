#!/usr/bin/env python3
""" Mini-Batch """

import tensorflow.compat.v1 as tf
shuffle_data = __import__('2-shuffle_data').shuffle_data


def train_mini_batch(X_train, Y_train, X_valid, Y_valid,
                     batch_size=32, epochs=5,
                     load_path="/tmp/model.ckpt", save_path="/tmp/model.ckpt"):
    """ trains a loaded neural network model
using mini-batch gradient descent """
    # import meta graph and restore session
    saver = tf.train.import_meta_graph(load_path + '.meta')
    sess = tf.Session()
    saver.restore(sess, load_path)

    # get tensors and ops from the collection restored
    x = tf.get_collection("x")[0]
    y = tf.get_collection("y")[0]
    accuracy = tf.get_collection("accuracy")[0]
    loss = tf.get_collection("loss")[0]
    train_op = tf.get_collection("train_op")[0]

    # loop over epochs
    for i in range(epochs):
        # shuffle data
        X_train, Y_train = shuffle_data(X_train, Y_train)
        step = 0
        # loop over the batches
        for j in range(0, m, batch_size):
            # get X_batch and Y_batch from data
            X_batch = X_train[j:j+batch_size]
            Y_batch = Y_train[j:j+batch_size]
            # train model
            sess.run(train_op, feed_dict={x: X_batch, y: Y_batch})
            step += 1
            if step % 100 == 0:
                step_cost, step_accuracy = sess.run([loss, accuracy], feed_dict={x: X_batch, y: Y_batch})
                print(f"\tStep {step}:")
                print(f"\t\tCost: {step_cost}")
                print(f"\t\tAccuracy: {step_accuracy}")
        train_cost, train_accuracy = sess.run([loss, accuracy], feed_dict={x: X_train, y: Y_train})
        valid_cost, valid_accuracy = sess.run([loss, accuracy], feed_dict={x: X_valid, y: Y_valid})
        print(f"After {i+1} epochs:")
        print(f"\tTraining Cost: {train_cost}")
        print(f"\tTraining Accuracy: {train_accuracy}")
        print(f"\tValidation Cost: {valid_cost}")
        print(f"\tValidation Accuracy: {valid_accuracy}")

    # save session
    saver.save(sess, save_path)
    return save_path
