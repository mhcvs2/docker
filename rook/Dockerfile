FROM registry.bst-1.cns.bstjpc.com:5000/rook/rook-xz:master

RUN apt-get update \
&& apt-get install xz-utils -y

COPY rook /usr/local/bin/rook
