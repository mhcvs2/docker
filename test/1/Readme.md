
debian:jessie  install 163 apt-get source
---------------
docker build --build-arg http_proxy=http://192.168.1.111:3142 --build-arg https_proxy=http://192.168.1.111:3142 -t debian_163:jessie .