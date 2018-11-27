FROM autoredis

EXPOSE 6379
ADD redis.conf /etc/redis/redis.conf
RUN chown redis:redis /etc/redis/redis.conf
COPY redis-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/redis-entrypoint.sh
ENTRYPOINT ["redis-entrypoint.sh"]