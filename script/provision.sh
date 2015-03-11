#!/usr/bin/env bash

apt-get update
apt-get install -y alien
alien -i /home/vagrant/oracle-instantclient11.1-basic-11.1.0.7.0-1.x86_64.rpm
alien -i /home/vagrant/cx_Oracle-5.1.2-11g-py27-1.x86_64.rpm
#TODO add links + install libaio1 and libpython2.7