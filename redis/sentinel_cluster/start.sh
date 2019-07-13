#!/usr/bin/env bash

docker run -p 6379:6379 -v /root/github/docker/redis/sentinel_cluster/redis.conf:/data/redis.conf --name redis-1 -d docker.io/redis redis-server redis.conf