./prometheus --storage.tsdb.path="/data/prometheus_data" \
--storage.tsdb.retention.time=15d \
--config.file="./prometheus.yml" > logs/run.log 2>&1 &