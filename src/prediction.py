#!/usr/bin/env python
import requests
from PIL import Image
import os, sys
import tensorflow as tf
import numpy as np

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

url = sys.argv[1]

r = requests.get(url, stream=True) #, stream=True)
r.raw.decode_content = True # Content-Encoding
im = Image.open(r.raw) #NOTE: it requires pillow 2.8+

# Read in the image_data
image_data = np.array(im)[:, :, 0:3]  # Select RGB channels only.

# Loads label file, strips off carriage return
label_lines = [line.rstrip() for line
                   in tf.gfile.GFile("model/retrained_labels.txt")]

# Unpersists graph from file
with tf.gfile.FastGFile("model/retrained_graph.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    tf.import_graph_def(graph_def, name='')

with tf.Session() as sess:
    # Feed the image_data as input to the graph and get first prediction
    softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

    predictions = sess.run(softmax_tensor, \
             {'DecodeJpeg:0': image_data})

    # Sort to show labels of first prediction in order of confidence
    top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

    for node_id in top_k:
        human_string = label_lines[node_id]
        score = predictions[0][node_id]
        print('%s (score = %.5f)' % (human_string, score))
