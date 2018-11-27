FROM $fromImage

COPY Percona-XtraBackup-2.4.8-r97330f7-jessie-x86_64-bundle.tar /Percona-XtraBackup-2.4.8-r97330f7-jessie-x86_64-bundle.tar
WORKDIR /
RUN dpkg -r percona-xtrabackup && dpkg -r percona-xtrabackup-dbg-24 && \
    tar -xf Percona-XtraBackup-2.4.8-r97330f7-jessie-x86_64-bundle.tar && \
    dpkg -i percona-xtrabackup-24_2.4.8-1.jessie_amd64.deb && \
    dpkg -i percona-xtrabackup-dbg-24_2.4.8-1.jessie_amd64.deb && \
    dpkg -i percona-xtrabackup-test-24_2.4.8-1.jessie_amd64.deb && \
    rm -rf /etc/mysql Percona-XtraBackup-2.4.8-r97330f7-jessie-x86_64-bundle.tar \
    percona-xtrabackup-24_2.4.8-1.jessie_amd64.deb \
    percona-xtrabackup-dbg-24_2.4.8-1.jessie_amd64.deb \
    percona-xtrabackup-test-24_2.4.8-1.jessie_amd64.deb

# configure ContainerPilot and MySQL

#RUN mkdir /var/lib/ansible
#COPY dbcm-base-manager-dbnode-mysql/dependency/ansible/module_executor.py /var/lib/ansible/module_executor.py
COPY ansible /var/lib/ansible
COPY dbcm-base-manager-dbnode-mysql/dependency/mysqld_exporter /usr/local/bin/mysqld_exporter
COPY dbcm-base-manager-dbnode-mysql/dependency/node_exporter /usr/local/bin/node_exporter

COPY dbcm-base-manager-dbnode-mysql/etc/* /etc/
COPY dbcm-base-manager-dbnode-mysql/bin/manager /usr/local/bin/manager
COPY dbcm-base-manager-dbnode-mysql/bin/test.py /usr/local/bin/test.py
COPY dbcm-base-manager-dbnode-mysql/bin/manage.py /usr/local/bin/manage.py

CMD ["/usr/local/bin/containerpilot"]