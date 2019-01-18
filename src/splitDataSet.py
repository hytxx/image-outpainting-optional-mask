#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Copyright (C) 2018 Topotek Ltd. All rights reserved.

Mail: hyt.lyy@gmail.com

File Name: dataset10000.py

Author: hyt

Created Time: 2018年12月26日 星期三 11时45分49秒

Description: reduces dataset from 36500 to 10000

'''

import os
import numpy as np
import shutil
import util

length = 250

filenames = os.listdir('./raw')
count = int(np.shape(filenames)[0] / length)

idx = [ [(i-1)*length, i*length] for i in range(1,count+1)]

filename = [np.asarray(filenames)[range(i[0], i[1])] for i in idx]
#filename = np.asarray(filenames)[idx]
#print(filename)

out_directory = [str(i[0])+'_'+str(i[1]) for i in idx]
#print(out_directory)


t = 0
for files in np.asarray(filename):
    os.makedirs(os.path.join(os.path.abspath('./data'), out_directory[t]))
    os.makedirs(os.path.join(os.path.abspath('./places_resized'), out_directory[t]))

    new_directory = os.path.join(os.path.abspath('./data'), out_directory[t])
    RSZ_PATH = os.path.join(os.path.abspath('./places_resized'), out_directory[t])
    OUT_PATH = os.path.join(os.path.abspath('./places'), out_directory[t] + '.npy')
    OUT_NPZ = os.path.join(os.path.abspath('./places'), out_directory[t] + '.npz')

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
    t +=1
