FROM ubuntu:18.04
WORKDIR /workspace
RUN apt-get update
RUN apt-get install python3.6 python3-pip vim