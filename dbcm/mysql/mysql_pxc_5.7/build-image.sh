#!/bin/sh

layer_names=(
    "pencona.base"
    "dependencies"
    "containerpilot"
    "belt"
)

no_build=(
    "percona:5.7"
    "autopilotpattern/mysql:5.7-1"
    "registry.bst-1.cns.bstjpc.com:5000/autopilotpattern/mysql-pxc:5.7-2"
)

source_dir=(
    ""
    ""
    ""
    "/root/gitSwarm/dbcm-base-manager-dbnode-pxc"
)

external_files=(
    "/root/GoglandProjects/beegoTest/src/git.sec.samsung.net/dbelt/dbcm-dbskeeper/bin/dbs_keeper"
)

base_name="dbelt/mysql-pxc-mysql-v5.7"

source ../../base.sh
