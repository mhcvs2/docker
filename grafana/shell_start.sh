#!/usr/bin/env bash

./bin/grafana-server --config="./config.ini" > /dev/null 2>&1 &

echo $! > tpid
echo Start Success!