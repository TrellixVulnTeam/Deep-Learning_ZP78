import tensorflow as tf
import numpy as np

tf.reset_default_graph()

# Create input data
X = np.random.randn(2, 10, 8)

# The second example is of length 6 
X[1,6:] = 0
X_lengths = [10, 6]

cell = tf.nn.rnn_cell.LSTMCell(num_units=64, state_is_tuple=True)

outputs, last_states = tf.nn.dynamic_rnn(
    cell=cell,
    dtype=tf.float64,
    sequence_length=X_lengths,
    inputs=X)

result = tf.contrib.learn.run_n(
    {"outputs": outputs, "last_states": last_states},
    n=1,
    feed_dict=None)

assert result[0]["outputs"].shape == (2, 10, 64)
print(result[0]["outputs"])

# Outputs for the second example past past length 6 should be 0
assert (result[0]["outputs"][1,7,:] == np.zeros(cell.output_size)).all()





import tensorflow as tf
import numpy as np

tf.reset_default_graph()

cell = tf.nn.rnn_cell.LSTMCell(num_units=64, state_is_tuple=True)

outputs, last_states = tf.nn.dynamic_rnn(
    cell=cell,
    dtype=tf.float64,
    sequence_length= [2, 1, 3],
    inputs=np.random.randn(3, 4, 0))


result = tf.contrib.learn.run_n(
    {"outputs": outputs, "last_states": last_states},
    n=1,
    feed_dict=None)

print(result[0]["outputs"])

