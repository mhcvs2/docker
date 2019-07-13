#!/usr/bin/env bash

docker run -p 6380:6380 -v /root/github/docker/redis/sentinel_cluster/redis2.conf:/data/redis.conf --name redis-2 -d docker.io/redis redis-server redis.conf