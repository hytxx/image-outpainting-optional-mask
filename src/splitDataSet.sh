#!/bin/sh

:<<!
Copyright (C) 2019 Topotek Ltd. All rights reserved.

Mail: hyt.lyy@gmail.com

File Name: splitDataSet.sh

Author: hyt

Created Time: 2019年01月17日 星期四 04时01分22秒

Description: 

!

rm -rf ./data/* && \
rm -rf ./places/* && \
rm -rf ./places_resized/* && \

python3 ./splitDataSet.py | tee splitDataSet.log
