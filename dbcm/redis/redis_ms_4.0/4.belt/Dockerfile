FROM $fromImage

# configure ContainerPilot and Redis

#RUN mkdir /var/lib/ansible
#COPY dbcm-base-manager-dbnode-mysql/dependency/ansible/module_executor.py /var/lib/ansible/module_executor.py
COPY ansible /var/lib/ansible
COPY dbcm-base-manager-dbnode-redis/dependency/redis_exporter /usr/local/bin/redis_exporter
COPY dbcm-base-manager-dbnode-redis/dependency/node_exporter /usr/local/bin/node_exporter

COPY dbcm-base-manager-dbnode-redis/etc/* /etc/
COPY dbcm-base-manager-dbnode-redis/bin/manager /usr/local/bin/manager
COPY dbcm-base-manager-dbnode-redis/bin/manage.py /usr/local/bin/manage.py
COPY dbcm-base-manager-dbnode-redis/bin/sentinel_reconfig_callback.py /usr/local/bin/sentinel_reconfig_callback.py
RUN chmod +x /usr/local/bin/sentinel_reconfig_callback.py

CMD ["/usr/local/bin/containerpilot"]
