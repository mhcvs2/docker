#!/usr/bin/env bash

openstack-config --set  /etc/glance/glance-registry.conf database connection mysql+pymysql://glance:mhc.123@ali/glance
openstack-config --set  /etc/glance/glance-registry.conf keystone_authtoken www_authenticate_uri http://v460:5000
openstack-config --set  /etc/glance/glance-registry.conf keystone_authtoken auth_url http://v460:5000
#openstack-config --set  /etc/glance/glance-registry.conf keystone_authtoken memcached_servers controller:11211
openstack-config --set  /etc/glance/glance-registry.conf keystone_authtoken auth_type password
openstack-config --set  /etc/glance/glance-registry.conf keystone_authtoken project_domain_name default
openstack-config --set  /etc/glance/glance-registry.conf keystone_authtoken user_domain_name default
openstack-config --set  /etc/glance/glance-registry.conf keystone_authtoken project_name service
openstack-config --set  /etc/glance/glance-registry.conf keystone_authtoken username glance
openstack-config --set  /etc/glance/glance-registry.conf keystone_authtoken password glance
openstack-config --set  /etc/glance/glance-registry.conf paste_deploy flavor keystone
