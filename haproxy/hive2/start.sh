#!/usr/bin/env bash

docker run -d --name=ha-hive -p9098:9098 -p9099:9099 -v/root/github/docker/haproxy/hive2:/usr/local/etc/haproxy haproxy:1.9
