FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip
RUN pip3 install --upgrade pip

RUN pip3 install pycryptodome

COPY . /app
WORKDIR /app
