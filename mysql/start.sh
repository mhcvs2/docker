#!/usr/bin/env bash

image=mysql:5.7
echo press password for mysql:
read pwd
password=${pwd}

conf_dir=/root/github/shell/mysql/conf.d
mysql_conf_dir=/root/github/shell/mysql/mysql.conf.d

docker run \
--name mysql \
-v /data/mysql-docker:/var/lib/mysql \
-v ${conf_dir}:/etc/mysql/conf.d \
-v ${mysql_conf_dir}:/etc/mysql/mysql.conf.d \
-e MYSQL_ROOT_PASSWORD=${password} \
-p 3306:3306 \
-d --restart=always ${image}
