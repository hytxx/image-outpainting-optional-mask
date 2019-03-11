#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Copyright (C) 2019 Topotek Ltd. All rights reserved.

Mail: hyt.lyy@gmail.com

File Name: read_tfrecords.py

Author: hyt

Created Time: 2019年03月09日 星期六 05时53分18秒

Description: 

'''

import os
import tensorflow as tf
import numpy as np


files = tf.train.match_filenames_once("./data/train_batch_tfrecords/*.tfrecords")
filename_queue = tf.train.string_input_producer(files, shuffle=False)

reader = tf.TFRecordReader()
_, serialized_example = reader.read(filename_queue)
features = tf.parse_single_example(
        serialized_example,
        features={
            "imgs_p": tf.FixedLenFeature([], dtype=tf.string)
            })      # 按照定义好的 features 协议解析 serialized_example 中的数据.

decoded_imgs_p = tf.decode_raw(features['imgs_p'], tf.uint8)

#init = tf.global_variables_initializer()
#init = tf.initialize_all_variables()
init_op = tf.local_variables_initializer()

with tf.Session() as sess:
    sess.run(init_op)

    print(sess.run(files))

    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)

    for i in range(10):
        print(sess.run(decoded_imgs_p))

    coord.request_stop()
    coord.join(threads)
