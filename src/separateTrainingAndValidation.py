#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Copyright (C) 2018 Topotek Ltd. All rights reserved.

Mail: hyt.lyy@gmail.com

File Name: separateTrainingAndValidation.py

Author: hyt

Created Time: 2018年12月25日 星期二 01时04分23秒

Description: 

'''

import numpy as np

data = np.load('places/all_images300.npy')

idx_test = np.random.choice(300, 100, replace=False)

idx_train = list(set(range(300)) - set(idx_test))

imgs_train = data[idx_train]

imgs_test = data[idx_test]

np.savez('places/places_300.npz', imgs_train=imgs_train, imgs_test=imgs_test, idx_train=idx_train, idx_test=idx_test)
