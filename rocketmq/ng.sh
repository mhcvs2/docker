#!/usr/bin/env bash

docker run \
-e "JAVA_OPTS=-Drocketmq.namesrv.addr=win7:9876 -Dcom.rocketmq.sendMessageWithVIPChannel=false" \
-p 8081:8080 -t -d \
--name ng \
styletang/rocketmq-console-ng