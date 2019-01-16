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


count = 300
out_directory = './dataset300'

filenames = os.listdir('./raw')
indexs = np.random.randint(0, np.shape(filenames)[0], count)
filename = np.asarray(filenames)[indexs]

for files in filename:
    full_outfilename = os.path.join(os.path.abspath('./raw'), files)
    print(full_outfilename)
    shutil.copy(full_outfilename, out_directory)
