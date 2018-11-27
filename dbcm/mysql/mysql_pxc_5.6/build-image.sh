#!/bin/sh

layer_names=(
    "pencona.base"
    "dependencies"
    "containerpilot"
    "belt"
)

no_build=(
    "no"
    "no"
    "registry.bst-1.cns.bstjpc.com:5000/autopilotpattern/mysql-pxc:5.6-2"
)

source_dir=(
    ""
    ""
    ""
    "/root/gitSwarm/dbcm-base-manager-dbnode-pxc"
)

external_files=(
    ""
)

base_name="registry.bst-1.cns.bstjpc.com:5000/dbelt/mysql-pxc-mysql-v5.6"

source ../../base.sh
