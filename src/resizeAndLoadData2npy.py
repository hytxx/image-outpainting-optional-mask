#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Copyright (C) 2018 Topotek Ltd. All rights reserved.

Mail: hyt.lyy@gmail.com

File Name: resizeAndLoadData2npy.py

Author: hyt

Created Time: 2018年12月25日 星期二 00时40分05秒

Description: 

'''

import util


IN_PATH, RSZ_PATH, OUT_PATH = './dataset300', 'places_resized', 'places/all_images300.npy'

util.resize_images(IN_PATH, RSZ_PATH)

util.compile_images(RSZ_PATH, OUT_PATH)


'''

import os
import numpy as np
import imageio
from PIL import Image


IMAGE_SZ = 128 # Should be a power of 2
src_PATH = './raw'
RSZ_PATH = './RSZ_PATH'
OUT_PATH = './places/all_images300.npy'

filenames = os.listdir(src_PATH)
for filename in filenames[:300]:  # 调试程序，取数据集前300个样本
    print('Processing %s' % filename)
    full_filename = os.path.join(os.path.abspath(src_PATH), filename)
    img_raw = Image.open(full_filename).convert('RGB')
    w, h = img_raw.size
    if w <= h:
        dim = w
        y_start = int((h - dim) / 2)
        img_crop = img_raw.crop(box=(0, y_start, dim, y_start + dim))
    else: # w > h
        dim = h
        x_start = int((w - dim) / 2)
        img_crop = img_raw.crop(box=(x_start, 0, x_start + dim, dim))
    img_scale = img_crop.resize((IMAGE_SZ, IMAGE_SZ), Image.ANTIALIAS)
    full_outfilename = os.path.join(os.path.abspath(RSZ_PATH), filename)
    img_scale.save(full_outfilename, format='PNG')

util.compile_images(RSZ_PATH, OUT_PATH)

'''
