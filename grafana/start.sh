#!/usr/bin/env bash

docker run -d --name grafana \
-p 3000:3000 \
-v /var/lib/grafana:/var/lib/grafana \
-e "GF_SECURITY_ADMIN_PASSWORD=secret" \
grafana/grafana:6.0.0