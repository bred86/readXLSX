FROM ubuntu:16.04

RUN apt-get update && \
  apt-get -y install python3-setuptools curl && \
  easy_install3 pip && \
  pip3 install elasticsearch openpyxl

COPY files /opt
