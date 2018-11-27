#!/bin/bash

layer_names=(
    "pencona.base"
    "dependencies"
    "containerpilot"
    "belt"
)

no_build=(
)

source_dir=(
    ""
    ""
    ""
    "../../../../dbcm-base-manager-dbnode-mysql"
)

external_files=(
    ""
)

base_name="dbelt/mysql-ms-mysql-v5.6.37-82"

source ../../base.sh

echo "Push the image to registry_server"
registry_server="registry.bst-1.cns.bstjpc.com:5000"
docker tag "$base_name$2" "$registry_server/$base_name:$2"
docker push "$registry_server/$base_name:$2"
