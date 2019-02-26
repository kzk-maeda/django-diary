FROM ubuntu:18.04

RUN apt-get -y update \
    && apt-get -y upgrade \
    && apt-get install -y locales curl python3-distutils \
    && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    && python3 get-pip.py \
    && pip install -U pip \
    && mkdir /code \
    && mkdir /root/.aws \
    && rm -rf /var/lib/apt/lists/* \
    && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8 \
    && pip install awscli --upgrade --user

ENV LANG en_US.utf8
ENV ACCESS_KEY dummy
ENV SECRET_ACCESS_KEY dummy

WORKDIR /root
ADD ./docker/config /root/.aws/
ADD ./docker/credentials /root/.aws/

WORKDIR /code
ADD ./docker/requirements.txt /code
RUN pip install -r requirements.txt
ADD application /code/application

CMD /usr/bin/python3 /code/application/manage.py runserver 8080
