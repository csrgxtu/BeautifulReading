# Version: 0.0.1
FROM ubuntu:14.04
MAINTAINER Archer Reilly "1246506786@qq.com"
RUN apt-get update
RUN apt-get install -y nginx
RUN echo 'Hi, I am in your container' \
  > /usr/share/nginx/html/index.html
EXPOSE 80
