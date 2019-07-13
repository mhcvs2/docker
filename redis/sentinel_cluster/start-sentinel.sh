

sudo docker run -p 26379:26379 -v /root/github/docker/redis/sentinel_cluster/sentinel.conf:/data/sentinel.conf --name redis-sentinel -d docker.io/redis redis-sentinel sentinel.conf

