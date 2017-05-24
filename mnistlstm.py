from __future__ import print_function

import tensorflow as tf
from tensorflow.python.ops import rnn, rnn_cell
import numpy as np

#Getting data
from tensorflow.examples.tutorials.mnist import input_data
mnist=input_data.read_data_sets("/tmp/data/", one_hot=True)

#Paramters
learning_rate=0.01
training_iter=100000
batch_size=128
display_step=10

#Network Parameters
n_input=28
n_steps=28
n_hidden=128
n_classes=10

#tf Graph
x=tf.placeholder("float",[None,n_steps,n_input])
y=tf.placeholder("float",[None,n_classes])

#Initializing weights
weights={
    'out':tf.Variable(tf.random_normal([2*n_hidden,n_classes]))
}
biases={
    'out':tf.Variable(tf.random_normal([n_classes]))
}

def RNN(x,weights,biases):

    x=tf.transpose(x,[1,0,2])
    x=tf.reshape(x,[-1,n_input])
    x=tf.split(0,n_steps,x)

    lstm_cell=rnn_cell.BasicLSTMCell(n_hidden,forget_bias=1.0)

    outputs,states=rnn.rnn(lstm_cell,x,dtype=tf.float32)

    return tf.matmul(outputs[-1],weights['out'])+biases['out']


def BiRNN(x, weights, biases):
    # Prepare data shape to match `bidirectional_rnn` function requirements
    # Current data input shape: (batch_size, n_steps, n_input)
    # Required shape: 'n_steps' tensors list of shape (batch_size, n_input)

    # Permuting batch_size and n_steps
    x = tf.transpose(x, [1, 0, 2])
    # Reshape to (n_steps*batch_size, n_input)
    x = tf.reshape(x, [-1, n_input])
    # Split to get a list of 'n_steps' tensors of shape (batch_size, n_input)
    x = tf.split(0, n_steps, x)

    # Define lstm cells with tensorflow
    # Forward direction cell
    lstm_fw_cell = rnn_cell.BasicLSTMCell(n_hidden, forget_bias=1.0)
    # Backward direction cell
    lstm_bw_cell = rnn_cell.BasicLSTMCell(n_hidden, forget_bias=1.0)

    # Get lstm cell output
    try:
        outputs, _, _ = rnn.bidirectional_rnn(lstm_fw_cell, lstm_bw_cell, x,
                                              dtype=tf.float32)
    except Exception:  # Old TensorFlow version only returns outputs not states
        outputs = rnn.bidirectional_rnn(lstm_fw_cell, lstm_bw_cell, x,
                                        dtype=tf.float32)

    # Linear activation, using rnn inner loop last output
    return tf.matmul(outputs[-1], weights['out']) + biases['out']

pred=BiRNN(x,weights,biases)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(pred, y))
optimizer=tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

#Evaluating Model
correct_pred=tf.equal(tf.argmax(pred,1),tf.argmax(y,1))
accuracy=tf.reduce_mean(tf.reduce_mean(tf.cast(correct_pred,tf.float32)))

#Model defined, now getting to running the session
init=tf.initialize_all_variables()

#Launching graph
with tf.Session() as sess:
    with tf.device('/cpu:0'):
        sess.run(init)
        step = 1
        # looping till iterations reached
        while step * batch_size < training_iter:
            batch_x, batch_y = mnist.train.next_batch(batch_size)
            # reshaping to 28sep of 28
            batch_x = batch_x.reshape((batch_size, n_steps, n_input))
            sess.run(optimizer, feed_dict={x: batch_x, y: batch_y})
            if step % display_step == 0:
                # batch accuracy
                acc = sess.run(accuracy, feed_dict={x: batch_x, y: batch_y})
                # batch loss
                loss = sess.run(cost, feed_dict={x: batch_x, y: batch_y})
                print("Iter " + str(step * batch_size) + ", Minibatch Loss= " + \
                      "{:06f}".format(loss) + ", Training Accuracy= " + \
                      "{:.5f}".format(acc))
            step += 1

    print("Optimization Complete")

    # Calculate accuracy for 128 mnist test images
    test_len = 128
    test_data = mnist.test.images[:test_len].reshape((-1, n_steps, n_input))
    test_label = mnist.test.labels[:test_len]
    print("Testing Accuracy:", \
      sess.run(accuracy, feed_dict={x: test_data, y: test_label}))