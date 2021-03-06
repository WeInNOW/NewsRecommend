import numpy as np
import tensorflow as tf

tf.reset_default_graph()
tf.set_random_seed(2016)
np.random.seed(2016)

# LSTM-autoencoder
from LSTMAutoencoder import *

# Constants
batch_num = 128
hidden_num = 12
step_num = 8
elem_num = 1
iteration = 100

# placeholder list
p_input = tf.placeholder(tf.float32, shape=(batch_num, step_num, elem_num))
p_inputs = [tf.squeeze(t, [1]) for t in tf.split(p_input, step_num, 1)]

cell = tf.nn.rnn_cell.LSTMCell(hidden_num, use_peepholes=True)
ae = LSTMAutoencoder(hidden_num, p_inputs, cell=cell, decode_without_input=True)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for i in range(iteration):
        """Random sequences.
          Every sequence has size batch_num * step_num * elem_num 
          Each step number increases 1 by 1.
          An initial number of each sequence is in the range from 0 to 19.
          (ex. [8. 9. 10. 11. 12. 13. 14. 15])
        """
        r = np.random.randint(20, size=batch_num).reshape([batch_num, 1, 1]) # 生成一个随机的值
        r = np.tile(r, (1, step_num, elem_num)) # 三维了；
        d = np.linspace(0, step_num, step_num, endpoint=False).reshape([1, step_num, elem_num])
        d = np.tile(d, (batch_num, 1, 1))
        random_sequences = r + d

        (loss_val, _) = sess.run([ae.loss, ae.train], {p_input: random_sequences})
        print('iter %d:' % (i + 1), loss_val)

    (input_, output_) = sess.run([ae.input_, ae.output_], {p_input: r + d})
    print('train result :')
    print('input :', input_[0, :, :].flatten())
    print('output :', output_[0, :, :].flatten())