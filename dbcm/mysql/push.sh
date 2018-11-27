#!/usr/bin/env bash

if [ "$1" != "" ]; then
    tag=$1
else
    tag="20171107"
fi

imgs=`docker images|awk '{print $1":"$2}'|grep "registry.bst-1.cns.bstjpc.com:5000"|grep $tag|grep -v $tag.1|grep -v $tag.2|grep -v $tag.3`


for img in ${imgs[@]}; do
    docker push $img
done