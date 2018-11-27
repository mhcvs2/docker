<<<<<<< HEAD:dbcm/mysql/mysql_ms_5.6.37-82/3.containerpilot/Dockerfile
FROM $fromImage
=======
FROM autopilotpattern/mysql:5.6-1
>>>>>>> 59e2be2d296010b14c206234c58e9d0a096db777:mysql5.6/2/Dockerfile

ENV CONTAINERPILOT_VER 3.4.2
ENV CONTAINERPILOT /etc/containerpilot.json5

# Add ContainerPilot
RUN set -ex \
    && export CONTAINERPILOT_CHECKSUM=5c99ae9ede01e8fcb9b027b5b3cb0cfd8c0b8b88 \
    && curl -Lsfo /tmp/containerpilot.tar.gz "https://github.com/joyent/containerpilot/releases/download/${CONTAINERPILOT_VER}/containerpilot-${CONTAINERPILOT_VER}.tar.gz" \
    && echo "${CONTAINERPILOT_CHECKSUM}  /tmp/containerpilot.tar.gz" | sha1sum -c \
    && tar zxf /tmp/containerpilot.tar.gz -C /usr/local/bin \
    && rm /tmp/containerpilot.tar.gz
