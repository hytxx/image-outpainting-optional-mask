#!/bin/sh

:<<!
Copyright (C) 2019 Topotek Ltd. All rights reserved.

Mail: xxx@topotel.com

File Name: gen.sh

Author: xxx

Created Time: 2019年01月16日 星期三 10时25分06秒

Description: 

!

python3 gen.py output/models/models/ output/models/models/model227000.ckpt.meta  ../images/images/city_128.png ./city1.png && \

python3 gen.py output/models/models/ output/models/models/model227000.ckpt.meta  ./city1.png ./city2.png && \

python3 gen.py output/models/models/ output/models/models/model227000.ckpt.meta  ./city2.png ./city3.png
