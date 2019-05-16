#!/usr/bin/env bash

docker run -d --name prometheus \
-p 9090:9090 \
-v /root/github/docker/prometheus/conf/prometheus.yml:/etc/prometheus/prometheus.yml \
-v /data/prometheus-data:/prometheus \
prom/prometheus:v2.7.1 \
--storage.tsdb.path="/prometheus" \
--storage.tsdb.retention.time=15d \
--config.file="/etc/prometheus/prometheus.yml"