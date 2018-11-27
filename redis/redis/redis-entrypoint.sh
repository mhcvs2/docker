#!/usr/bin/env bash

if test -z $MASTER; then
    sed -i '$d' /etc/redis/redis.conf
else
    sed -i "s/\$MASTER/$MASTER/g" /etc/redis/redis.conf
fi

exec docker-entrypoint.sh redis-server /etc/redis/redis.conf



