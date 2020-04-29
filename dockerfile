FROM ubuntu:18.04
WORKDIR /workspace
RUN apt-get update
RUN apt-get install python3.6 python3-pip vim
RUN git clone https://github.com/Elinole/m1python.git
RUN pip3 install jupyter
RUN pip3 install notebook
RUN pip3 install pandas
RUN pip3 install numpy
EXPOSE 8000