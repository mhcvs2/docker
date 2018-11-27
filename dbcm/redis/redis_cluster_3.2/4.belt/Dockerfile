FROM $fromImage
# configure ContainerPilot and Redis

#RUN mkdir /var/lib/ansible
#COPY dbcm-base-manager-dbnode-mysql/dependency/ansible/module_executor.py /var/lib/ansible/module_executor.py
COPY ansible /var/lib/ansible
COPY dbcm-base-manager-dbnode-rediscluster/dependency/redis_exporter /usr/local/bin/redis_exporter
COPY dbcm-base-manager-dbnode-rediscluster/dependency/node_exporter /usr/local/bin/node_exporter

COPY dbcm-base-manager-dbnode-rediscluster/etc/* /etc/
COPY dbcm-base-manager-dbnode-rediscluster/bin/manager /usr/local/bin/manager
COPY dbcm-base-manager-dbnode-rediscluster/bin/manage.py /usr/local/bin/manage.py

CMD ["/usr/local/bin/containerpilot"]
