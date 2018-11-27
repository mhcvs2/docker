FROM $fromImage

ENV CONTAINERPILOT_VER 3.4.2
ENV CONTAINERPILOT /etc/containerpilot.json5

# Add ContainerPilot
RUN set -ex \
    && export CONTAINERPILOT_CHECKSUM=5c99ae9ede01e8fcb9b027b5b3cb0cfd8c0b8b88 \
    && curl -Lsfo /tmp/containerpilot.tar.gz "https://github.com/joyent/containerpilot/releases/download/${CONTAINERPILOT_VER}/containerpilot-${CONTAINERPILOT_VER}.tar.gz" \
    && echo "${CONTAINERPILOT_CHECKSUM}  /tmp/containerpilot.tar.gz" | sha1sum -c \
    && tar zxf /tmp/containerpilot.tar.gz -C /usr/local/bin \
    && rm /tmp/containerpilot.tar.gz
