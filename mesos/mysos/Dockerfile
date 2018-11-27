FROM mesos:1.3.0

RUN yum update \
&& yum install wget -y \
&& wget http://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm \
&& rpm -ivh epel-release-latest-7.noarch.rpm \
&& rm -rf epel-release-latest-7.noarch.rpm \
&& yum repolist \
&& yum install python-pip -y \
&& yum install gcc -y \
&& yum install python-devel -y \
&& yum install libffi-devel -y \
&& yum install numpy -y \
&& yum install libtool -y\
&& yum install make -y
