#!/usr/bin/env bash

apt-get update
apt-get install -y alien
alien -i /home/vagrant/oracle-instantclient11.1-basic-11.1.0.7.0-1.x86_64.rpm
alien -i /home/vagrant/cx_Oracle-5.1.2-11g-py27-1.x86_64.rpm
apt-get install -y libpython2.7
apt-get install -y libaio1
ln -s /usr/lib/python2.7/site-packages/cx_Oracle.so /usr/lib/python2.7/lib-dynload
ln -s /usr/lib/oracle/11.1/client64/lib/libnnz11.so /usr/lib
ln -s /usr/lib/oracle/11.1/client64/lib/libclntsh.so.11.1 /usr/lib
#echo export LD_LIBRARY_PATH=/usr/lib/oracle/11.1/client/lib >> ~/.bashrc
#source ~/.bashrc
