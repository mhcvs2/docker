#!/usr/bin/env bash

docker run -d --name prometheus \
-p 9090:9090 \
-v /root/github/docker/prometheus/conf/prometheus.yml:/etc/prometheus/prometheus.yml \
prom/prometheus:v2.7.1