FROM mesosphere/mesos-slave:1.1.1

RUN apt-get update \
&& apt-get upgrade -y

RUN apt-get install vim python-pip -y
export PYTHONPATH=/usr/lib/python2.7/site-packages