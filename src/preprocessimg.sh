#!/bin/sh

:<<!
Copyright (C) 2018 Topotek Ltd. All rights reserved.

Mail: hyt.lyy@gmail.com

File Name: preprocessimg.sh

Author: hyt

Created Time: 2018年12月30日 星期日 00时51分13秒

Description: 

!

rm -rf ./dataset300/* && \
rm -rf ./places_resized/* && \
rm -rf ./places/*

python3 ./dataset300.py && \
python3 ./resizeAndLoadData2npy.py && \
python3 ./separateTrainingAndValidation.py
