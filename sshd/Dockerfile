FROM registry.bst-1.cns.bstjpc.com:5000/ubuntu:14.04

RUN apt-get update \
&& apt-get install -y openssh-server \
&& mkdir -p /var/run/sshd \
&& mkdir -p /root/.ssh \
&& sed -ri 's/session    required     pam_loginuid.so/#session    required     pam_loginuid.so/g' /etc/pam.d/sshd

COPY authorized_keys /root/.ssh/authorized_keys
COPY run.sh /run.sh

EXPOSE 22

RUN chmod +x /run.sh

CMD ["/run.sh"]



