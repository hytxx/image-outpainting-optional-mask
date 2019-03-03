#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Copyright (C) 2019 Topotek Ltd. All rights reserved.

Mail: hyt.lyy@gmail.com

File Name: recovertfcords.py

Author: hyt

Created Time: 2019年03月04日 星期一 00时31分45秒

Description: 

'''

import os
import tensorflow as tf
from PIL import Image
import numpy as np

save_path = "./data/Recorvertfrecords/"
if not os.path.exists(save_path):
    os.makedirs(save_path)


filename_queue = tf.train.string_input_producer(["./data/imgs_resized_test.tfrecords"])
reader = tf.TFRecordReader()
_, serialized_example = reader.read(filename_queue)

features = tf.parse_single_example(serialized_example,
        features={
            'img_raw': tf.FixedLenFeature([], tf.string),
            })

image = tf.decode_raw(features['img_raw'], tf.uint8)
image = tf.reshape(image, [128, 128, 3])
with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(coord=coord)
    for i in range(10):
        example = sess.run([image])
        #print(example)
        print(np.shape(example))
        img = Image.fromarray(example[0], 'RGB')
        img.save(save_path + str(i) + '_test' + '.jpg' )
        print(example)
    coord.request_stop()
    coord.join(threads)

