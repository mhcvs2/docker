#!/usr/bin/env bash

dir=`pwd`

cd $dir/mysql_ms_5.6
./build-image.sh

cd $dir/mysql_ms_5.7
./build-image.sh

cd $dir/mysql_pxc_5.6
./build-image.sh

cd $dir/../redis/redis_cluster_3.2
./build-image.sh

cd $dir/../redis/redis_ms_3.2
./build-image.sh

cd $dir/../redis/redis_ms_4.0
./build-image.sh