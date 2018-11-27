#!/bin/sh

layer_names=(
    "redis.base"
    "dependencies"
    "containerpilot"
    "belt"
)

no_build=(
    "no"
    "no"
    "registry.bst-1.cns.bstjpc.com:5000/autopilotpattern/redis-trib:3.2-2"
)

source_dir=(
    ""
    ""
    ""
    "/root/gitSwarm/dbcm-base-manager-dbnode-rediscluster"
)

external_files=(
    ""
)

base_name="registry.bst-1.cns.bstjpc.com:5000/dbelt/redis-cluster-redis-v3.2"

source ../../base.sh
