#!/usr/bin/env bash

base_dir=`pwd`

VER=$1
TAG=$2

check_img(){
    name=$1
    CHECKIMG=""
    imgs=`docker images|awk '{print $1":"$2}'`
    for img in ${imgs[@]}; do
        if [ "$img" = "$name" ]; then
            CHECKIMG="yes"
            #CHECKIMG=""
        fi
    done

}

rollback(){
    echo "rollback..."
    sed -i 's@'"$IMAGE.$pre"'@\$fromImage@' Dockerfile
    remove_source
    exit 0
}

docker_build(){
    cmd="docker build -t ${img_name}"
    if [ "$PROXY" != "" ]; then
        cmd=${cmd}" --build-arg $PROXY"
    fi
    if [ "$PROXYS" != "" ]; then
	cmd=${cmd}" --build-arg $PROXYS"
    fi

    cmd=${cmd}" ."    

    echo $cmd
    eval $cmd
    sleep 2
    if [ $? -ne 0 ]; then
        rollback
    fi
}

copy_source(){
    dir_path=${source_dir[$((i-1))]}
    echo $dir_path
    if [ "$dir_path" != "" ]; then
        if ! test -d $dir_path; then
            echo "$dir_path do not exist"
            exit 1
        fi
        cp -r $dir_path .
    fi
    if ! test -d ./external_files; then
        mkdir ./external_files
    fi
    for external_file in ${external_files[@]}; do
        if ! test -f $external_file; then
            echo "$external_file do not exist or not a file, passed"
            continue
        fi
        cp $external_file ./external_files
    done
}

remove_source(){
    dir_name=${dir_path##*/}
    if ! test -z $dir_name; then
        rm -rf ./$dir_name
    fi
    if test -d ./external_files; then
        rm -rf ./external_files
    fi
}

trap rollback INT

if [ "$#" -le 1 ]; then
  TAG=`date +"%Y%m%d"`
  echo "No tag info, the default is current date:$TAG"
fi
if [ "$#" -le 0 ]; then
  VER="v0.2.0"
  echo "No versiong info, the default version is $VER"
fi
PROXY=""
if ! [ -z "$http_proxy" ]; then
   echo "Buidling the image via the proxy $http_proxy"
   PROXY="http_proxy=$http_proxy"
fi
if ! [ -z "$https_proxy" ]; then
   echo "Buidling the image via the proxys $https_proxy"
   PROXYS="https_proxy=$https_proxy"
fi
IMAGE=$base_name-$VER:$TAG

untag=()

len=${#layer_names[@]}
for ((i=1;i<=$len;i++))
do
    if [ $i -eq $len ]; then
        img_name=$IMAGE
    else
        img_name=$IMAGE.$i
    fi
    if [ "${no_build[$((i-1))]}" != "" ]; then
        if [ "${no_build[$((i-1))]}" = "no" ]; then
            continue
        fi
        check_img ${no_build[$((i-1))]}
        if [ -z "$CHECKIMG" ]; then
            echo "no image ${no_build[$((i-1))]}"
            exit 1
        fi
        docker tag ${no_build[$((i-1))]} $img_name
        untag[$((i-1))]=$img_name
    fi
    check_img $img_name
    if [ -z "$CHECKIMG" ]; then
        echo "Starting to build $img_name"
        act_dir=$base_dir/$i.${layer_names[$((i-1))]}
        if ! test -d $act_dir; then
            echo "$act_dir do not exist"
            exit 1
        fi
        cd $act_dir
        copy_source
        pre=$((i-1))
        sed -i 's@\$fromImage@'"$IMAGE.$pre"'@' Dockerfile
        docker_build
        sed -i 's@'"$IMAGE.$pre"'@\$fromImage@' Dockerfile
        remove_source
    fi
done

for img in ${untag[@]}; do
    if [ "$img" != "" ]; then
        docker rmi $img 2>&1 >/dev/null
    fi
done
