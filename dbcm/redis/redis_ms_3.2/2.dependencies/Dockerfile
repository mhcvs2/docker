FROM $fromImage

# By keeping a lot of discrete steps in a single RUN we can clean up after
# ourselves in the same layer. This is gross but it saves ~100MB in the image
WORKDIR /
RUN set -ex \
    && export buildDeps='python-dev gcc unzip' \
    && export runDeps='python curl libffi-dev libssl-dev ca-certificates' \
    && apt-get update \
    && apt-get install -y $buildDeps $runDeps --no-install-recommends \
    && curl -Lsfo get-pip.py https://bootstrap.pypa.io/get-pip.py \
    && python get-pip.py \
    && pip install \
       python-Consul==0.7.0 \
       manta==2.5.0 \
       minio==2.2.4 \
       mock==2.0.0 \
       json5==0.2.4 \
       prometheus_client==0.0.20 \
       redis \
    # \
    # Add Consul from https://releases.hashicorp.com/consul \
    # \
    && export CHECKSUM=c8859a0a34c50115cdff147f998b2b63226f5f052e50f342209142420d1c2668 \
    && curl -Lsfo /tmp/consul.zip https://releases.hashicorp.com/consul/0.8.4/consul_0.8.4_linux_amd64.zip \
    && echo "${CHECKSUM}  /tmp/consul.zip" | sha256sum -c \
    && unzip /tmp/consul.zip -d /usr/local/bin \
    && rm /tmp/consul.zip \
    && mkdir /config \
    # \
    # clean up to minimize image layer size \
    # \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get purge -y --auto-remove $buildDeps \
    && rm /get-pip.py \
    && rm /usr/local/bin/docker-entrypoint.sh

# override the parent entrypoint
ENTRYPOINT []