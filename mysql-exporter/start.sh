#!/usr/bin/env bash

image=quintoandar/mysqld_exporter

docker run \
--name me \
-v /root/github/docker/mysql-exporter/my.cnf:/etc/my.cnf \
-p 9104:9104 \
-d --restart=always ${image} --config.my-cnf=/etc/my.cnf
