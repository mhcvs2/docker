#!/usr/bin/env bash

image=minio/minio

docker run \
--name mysql \
-v /data/minio:/data \
-e MINIO_ACCESS_KEY=mhc \
-e MINIO_SECRET_KEY=qq77aa88 \
-p 9000:9000 \
-d --restart=always ${image} server /data
