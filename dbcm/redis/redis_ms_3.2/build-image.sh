#!/bin/sh

layer_names=(
    "redis.base"
    "dependencies"
    "containerpilot"
    "belt"
)

no_build=(
    "redis:3.2.10-alpine"
    "autopilotpattern/redis:3.2.10-1"
    "registry.bst-1.cns.bstjpc.com:5000/autopilotpattern/redis:3.2.10-2"
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

base_name="registry.bst-1.cns.bstjpc.com:5000/dbelt/redis-ms-redis-v3.2"

source ../../base.sh
