#!/usr/bin/env python3
""" Mini-Batch """
import tensorflow.compat.v1 as tf


shuffle_data = __import__('2-shuffle_data').shuffle_data


def train_mini_batch(X_train, Y_train, X_valid, Y_valid,
                     batch_size=32, epochs=5,
                     load_path="/tmp/model.ckpt",
                     save_path="/tmp/model.ckpt"):
    """ trains a loaded neural network model
using mini-batch gradient descent """
    with tf.Session() as sess:
        n = X_train.shape[0]
        batch = n // batch_size
        # import meta graph and restore session
        saver = tf.train.import_meta_graph(load_path + '.meta')
        saver.restore(sess, load_path)

        # get tensors and ops from the collection restored
        x = tf.get_collection("x")[0]
        y = tf.get_collection("y")[0]
        accuracy = tf.get_collection("accuracy")[0]
        loss = tf.get_collection("loss")[0]
        train_op = tf.get_collection("train_op")[0]

        if batch % batch_size != 0:
            batch += 1
        # loop over epochs
        for i in range(epochs + 1):
            # shuffle data
            X_train, Y_train = shuffle_data(X_train, Y_train)
            step = 0
            train_cost = loss.eval({x: X_train, y: Y_train})
            train_accuracy = accuracy.eval({x: X_train, y: Y_train})
            valid_cost = loss.eval({x: X_valid, y: Y_valid})
            valid_accuracy = accuracy.eval({x: X_valid, y: Y_valid})
            print("After {} epochs:".format(i))
            print("\tTraining Cost: {}".format(train_cost))
            print("\tTraining Accuracy: {}".format(train_accuracy))
            print("\tValidation Cost: {}".format(valid_cost))
            print("\tValidation Accuracy: {}".format(valid_accuracy))
            if i == epochs:
                break
            # loop over the batches
            for j in range(batch):
                # get X_batch and Y_batch from data
                X_batch = X_train[j*batch_size:(j+1)*batch_size]
                Y_batch = Y_train[j*batch_size:(j+1)*batch_size]
                # train model
                sess.run(train_op, feed_dict={x: X_batch, y: Y_batch})
                if (j+1) % 100 == 0 and j != 0:
                    print("\tStep {}:".format(j+1))
                    step_cost = loss.eval({x: X_batch, y: Y_batch})
                    step_accuracy = accuracy.eval({x: X_batch, y: Y_batch})
                    print("\t\tCost: {}".format(step_cost))
                    print("\t\tAccuracy: {}".format(step_accuracy))
        # save session
        return saver.save(sess, save_path)
