FROM $fromImage

# configure ContainerPilot and MySQL

RUN rm -rf /etc/mysql/my.cnf
#RUN mkdir /var/lib/ansible
#COPY dbcm-base-manager-dbnode-mysql/dependency/ansible/module_executor.py /var/lib/ansible/module_executor.py
COPY ansible /var/lib/ansible
COPY dbcm-base-manager-dbnode-pxc/dependency/mysqld_exporter /usr/local/bin/mysqld_exporter
COPY dbcm-base-manager-dbnode-pxc/dependency/node_exporter /usr/local/bin/node_exporter

COPY dbcm-base-manager-dbnode-pxc/etc/* /etc/
COPY dbcm-base-manager-dbnode-pxc/bin/manager /usr/local/bin/manager
COPY dbcm-base-manager-dbnode-pxc/bin/test.py /usr/local/bin/test.py
COPY dbcm-base-manager-dbnode-pxc/bin/manage.py /usr/local/bin/manage.py

CMD ["/usr/local/bin/containerpilot"]