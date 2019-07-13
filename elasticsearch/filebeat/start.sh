#!/usr/bin/env bash

./filebeat -e -c filebeat.yml -d "publish" > /dev/null 2>&1 &

echo $! > tpid
echo Start Success!