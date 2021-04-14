#!/usr/bin/env bash

image=quintoandar/mysqld_exporter

docker run \
--name me \
-v /root/github/docker/mysql-exporter/my.cnf:/etc/my.cnf \
-p 9104:9104 \
-e DB_USER=root \
-e DB_PASSWORD=qq77aa88 \
-e DB_DNS=192.168.141.129 \
-e DB_PORT=3306 \
-d --restart=always ${image}
