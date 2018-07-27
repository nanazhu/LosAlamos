import warnings
warnings.filterwarnings("ignore")
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
import numpy as np

# making up some random data
x_data = np.linspace(-1,1,300)[:,np.newaxis] # flatten your arrary into list
noise = np.random.normal(0,0.05,x_data.shape)
y_data = np.square(x_data)-0.5+noise


with tf.name_scope('input_layer'):
    x = tf.placeholder(tf.float32,[None,1],name='x_input')
    y = tf.placeholder(tf.float32,[None,1],name='y_input')

with tf.name_scope('hidden_layer'):
    with tf.name_scope('W'):
        W1 = tf.Variable(tf.random_normal([1,10]))
        tf.summary.histogram('hidden-weight',W1)

    with tf.name_scope('B'):
        b1 = tf.constant(0.5,shape=[1,10])
        tf.summary.histogram('hidden-bias',b1)

    with tf.name_scope('Activation'):
        a = tf.matmul(x,W1)+b1
        tf.summary.histogram('hidden-pre-active',a)

hidden = tf.nn.sigmoid(a)
tf.summary.histogram('hidden-activation',hidden)

with tf.name_scope('output_layer'):
    with tf.name_scope('W'):
        W2 = tf.Variable(tf.random_normal([10,1]))
        tf.summary.histogram('output-weight', W2)

    with tf.name_scope('B'):
        b2 = tf.constant(0.1, shape=[1, 1])
        tf.summary.histogram('output-bias', b2)

    with tf.name_scope('Activation'):
        a = tf.matmul(hidden, W2) + b2
        tf.summary.histogram('output-pre-active', a)

output = tf.nn.softmax(a)
tf.summary.histogram('output-activation', output)


with tf.name_scope('loss'):
    loss = tf.losses.sigmoid_cross_entropy(y_data,output)
    tf.summary.scalar('loss',loss)


with tf.name_scope('train'):
    train = tf.train.AdamOptimizer().minimize(loss)

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    merge = tf.summary.merge_all()
    writer = tf.summary.FileWriter('demo_log',sess.graph)

    for i in range(10000) :
        sess.run(train,feed_dict={x:x_data,y:y_data})
        if (i%20 == 0 ):
            result = sess.run(merge,feed_dict={x:x_data,y:y_data})
            writer.add_summary(result,i)