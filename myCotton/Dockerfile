FROM mesosphere/mesos-slave:1.1.1

RUN apt-get update \
&& apt-get upgrade -y

ENV PYTHONPATH /usr/lib/python2.7/site-packages

RUN apt-get install vim python-dev python-pip -y

RUN apt-get install python-numpy=1:1.8.2-0ubuntu0.1 libffi-dev -y