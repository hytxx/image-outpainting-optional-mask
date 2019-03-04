#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Copyright (C) 2018 Topotek Ltd. All rights reserved.

Mail: hyt.lyy@gmail.com

File Name: splitDataSet.py

Author: hyt

Created Time: 2018年12月26日 星期三 11时45分49秒

Description: 把数据集分批次处理

'''

import os
import numpy as np
import shutil
import util
from PIL import Image
import tensorflow as tf
import threading
import util


filenames = os.listdir('./raw')
datalenth = len(filenames)
imgs_path = [os.path.join(os.path.abspath('./raw'), filename) for filename in filenames]
imgs_train_dir = './data/imgs_train'
imgs_test_dir = './data/imgs_test'
imgs_resized_test = './data/imgs_resized_test'
imgs_resized_train = './data/imgs_resized_train'

tfrecords_test = "./data/imgs_resized_test.tfrecords"
tfrecords_train = "./data/imgs_resized_train.tfrecords"

tfrecords_test_imgs_p = "./data/tfrecords_test_imgs_p.tfrecords"
tfrecords_train_imgs_p = "./data/tfrecords_train_imgs_p.tfrecords"

how2test = 100

if not os.path.exists(imgs_train_dir):
    os.makedirs(os.path.abspath(imgs_train_dir))
if not os.path.exists(imgs_test_dir):
    os.makedirs(os.path.abspath(imgs_test_dir))
if not os.path.exists(imgs_resized_train):
    os.makedirs(os.path.abspath(imgs_resized_train))
if not os.path.exists(imgs_resized_test):
    os.makedirs(os.path.abspath(imgs_resized_test))


def spilt250():    
    length = 250

    count = int(np.shape(filenames)[0] / length)

    idx = [ [(i-1)*length, i*length] for i in range(1,count+1)]

    filename = [np.asarray(filenames)[range(i[0], i[1])] for i in idx]
    #filename = np.asarray(filenames)[idx]
    #print(filename)

    out_directory = [str(i[0])+'_'+str(i[1]) for i in idx]
    #print(out_directory)


    for idx, files in enumerate(filename):
        os.makedirs(os.path.join(os.path.abspath('./data'), out_directory[idx]))
        os.makedirs(os.path.join(os.path.abspath('./places_resized'), out_directory[idx]))

        new_directory = os.path.join(os.path.abspath('./data'), out_directory[idx])
        RSZ_PATH = os.path.join(os.path.abspath('./places_resized'), out_directory[idx])
        OUT_PATH = os.path.join(os.path.abspath('./places'), out_directory[idx] + '.npy')
        OUT_NPZ = os.path.join(os.path.abspath('./places'), out_directory[idx] + '.npz')

        print(new_directory)
        for file_i in np.asarray(files):
            full_outfilename = os.path.join(os.path.abspath('./raw'), file_i)
            print(full_outfilename)
            shutil.copy(full_outfilename, new_directory)

        util.resize_images(new_directory, RSZ_PATH)
        util.compile_images(RSZ_PATH, OUT_PATH)

        data = np.load(OUT_PATH)
        idx_test = np.random.choice(length, 1, replace=False)
        idx_train = list(set(range(length)) - set(idx_test))
        imgs_train = data[idx_train]
        imgs_test = data[idx_test]
        np.savez(OUT_NPZ, imgs_train=imgs_train, imgs_test=imgs_test, idx_train=idx_train, idx_test=idx_test)


def split2tfrecoder():
    idx_test = np.random.choice(datalenth, how2test, replace=False) 
    idx_train = list(set(range(datalenth)) - set(idx_test))
    print("idx_test = %d" % (len(idx_test)))
    print("idx_train = %d" % (len(idx_train)))
    print('imgs_path length = %d' % len(imgs_path))
    for idx in idx_train:
        shutil.copy(imgs_path[idx], imgs_train_dir)
    util.resize_images(imgs_train_dir, imgs_resized_train)

    for idx in idx_test:
        shutil.copy(imgs_path[idx], imgs_test_dir)
    util.resize_images(imgs_test_dir, imgs_resized_test)


def writePreprocess_images_outpainting(imgs_PATH, write_path, crop=True, position='middle'):
    imgs = util.load_images(imgs_PATH)    # imgs_PATH can be imgs_resized_train  or imgs_resized_test
    imgs_p = util.preprocess_images_outpainting(imgs, crop, position)
    writer = tf.python_io.TFRecordWriter(write_path)    # write_path can be tfrecords_train_imgs_p  or tfrecords_test_imgs_p
    for img_p in imgs_p:

    



def writetfrecords(write_path, image_path):

    '''
    write_path:  tfrecords_train  or tfrecords_test 
    image_path:  imgs_resized_train or imgs_resized_test 

    '''
    writer = tf.python_io.TFRecordWriter(write_path)
    for img_name in os.listdir(image_path):
        img_abspath = os.path.join(os.path.abspath(image_path), img_name)
        img = Image.open(img_abspath)
        img_raw = img.tobytes()     # 将图片转换为二进制
        example = tf.train.Example(features=tf.train.Features(
            feature={"img_raw": tf.train.Feature(bytes_list=tf.train.BytesList(value=[img_raw]))}
            ))
        writer.write(example.SerializeToString())
        #print("当前正在运行的线程数量 %d" % threading.activeCount())
        #print('current thread  >>> %s ' % threading.current_thread().name)
        #print(threading.enumerate())

    writer.close()


if __name__ == '__main__':
    #coord = tf.train.Coordinator()
    #threads = [threading.Thread(target=split2tfrecoder, args=(coord,)) for i in range(8)]
    #for t in threads: t.start()
    #coord.join(threads)

    split2tfrecoder()
    writetfrecords(tfrecords_train, imgs_resized_train)
    writetfrecords(tfrecords_test, imgs_resized_test)
