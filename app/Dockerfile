FROM python:3

RUN apt-get update

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN apt-get -y --fix-missing install vim wget curl unzip

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

USER root
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm
