# credit :  Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
import warnings
warnings.filterwarnings("ignore")
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf

def add_layer(inputs, in_size, out_size, activation_function=None,layername = 'layer'):
    # add one more layer and return the output of this layer
    with tf.name_scope(layername):
        with tf.name_scope('weights'):
            Weights = tf.Variable(tf.random_normal([in_size, out_size]), name='W')
        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1, out_size]) + 0.1, name='b')
        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b = tf.add(tf.matmul(inputs, Weights), biases)
        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b, )
        return outputs

# define placeholder for inputs to network
with tf.name_scope('inputs'):
    xs = tf.placeholder(tf.float32, [None, 1], name='x_input')
    ys = tf.placeholder(tf.float32, [None, 1], name='y_input')

# add hidden layer
l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu,layername='hidden')
# add output layer
prediction = add_layer(l1, 10, 1, activation_function=tf.nn.sigmoid,layername='output')

# the error between prediciton and real data
with tf.name_scope('loss'):
    # loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),
    #                                     reduction_indices=[1]))
    loss = tf.reduce_max(tf.losses.mean_squared_error(predictions=prediction,labels=ys))
    tf.summary.scalar('loss',loss)
with tf.name_scope('train'):
    train = tf.train.AdamOptimizer(0.1).minimize(loss)

with tf.Session() as sess:


    init = tf.global_variables_initializer()

    writer = tf.summary.FileWriter("logs", sess.graph)
    # sess.run(init)
    summary = tf.summary.merge_all()
    _, summary = sess.run([init,summary])
    writer.add_summary(summary)
# direct to the local dir and run this in terminal:
# $ tensorboard --logdir=logs


