#!/bin/sh

layer_names=(
    "redis.base"
    "dependencies"
    "containerpilot"
    "belt"
)

no_build=(
    "redis:4.0-alpine"
    "autopilotpattern/redis:4.0-1"
    "registry.bst-1.cns.bstjpc.com:5000/autopilotpattern/redis:4.0-2"
)

source_dir=(
    ""
    ""
    ""
    "/root/gitSwarm/dbcm-base-manager-dbnode-redis"
)

external_files=(
    ""
)

base_name="registry.bst-1.cns.bstjpc.com:5000/dbelt/redis-ms-redis-v4.0"

source ../../base.sh
