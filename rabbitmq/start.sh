#!/usr/bin/env bash

docker run -d \
--hostname my-rabbit \
--name my-rabbit \
-p 8080:15672 \
-p 5672:5672 \
-v /data/rabbitmq-docker:/var/lib/rabbitmq \
-e RABBITMQ_DEFAULT_USER=mhc \
-e RABBITMQ_DEFAULT_PASS=mhc.123 \
rabbitmq:3-management