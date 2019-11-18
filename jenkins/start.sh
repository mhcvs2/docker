#!/usr/bin/env bash

mkdir -p /data/jenkins

docker run -p 8080:8080 -p 50000:50000 -v /data/jenkins:/var/jenkins_home jenkins:2.60.3


