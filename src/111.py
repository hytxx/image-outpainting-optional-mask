#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Copyright (C) 2019 Topotek Ltd. All rights reserved.

Mail: hyt.lyy@gmail.com

File Name: 111.py

Author: hyt

Created Time: 2019年03月10日 星期日 17时40分00秒

Description: 

'''

import tensorflow as tf
import os
import numpy as np


filename_queue = tf.train.string_input_producer(["./data/train_batch_tfrecords/1040_2080.tfrecords"])

reader = tf.TFRecordReader()
_, serialized_example = reader.read(filename_queue)

features = tf.parse_single_example(
        serialized_example,
        features={
            "imgs_p": tf.FixedLenFeature([], tf.string)
            })

init_op = tf.initialize_all_variables()

imgs_p_Parsed = tf.decode_raw(features["imgs_p"], tf.uint8)

with tf.Session() as sess:
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)
    sess.run(init_op)
    print(sess.run(features))
    #print(sess.run(imgs_p_Parsed))
