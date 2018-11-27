FROM registry.bst-1.cns.bstjpc.com:5000/chaneyk/tensorflow-cuda9:latest-gpu

RUN apt-get update \
&& apt-get install -y openssh-server \
&& mkdir -p /var/run/sshd \
&& mkdir -p /root/.ssh \
&& sed -ri 's/session    required     pam_loginuid.so/#session    required     pam_loginuid.so/g' /etc/pam.d/sshd

COPY run.sh /run.sh
COPY run_jupyter.sh /run_jupyter.sh

EXPOSE 22

RUN chmod +x /run.sh
RUN chmod +x /run_jupyter.sh
RUN sed -i '$a export http_proxy=109.105.1.52:8080' /root/.bashrc \
&& sed -i '$a export https_proxy=109.105.1.52:8080' /root/.bashrc


CMD ["/run.sh"]



