FROM python:2
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install pip --upgrade && pip install -r requirements.txt
ADD . /code/

RUN apt-get update 
RUN apt-get install -y cron --force-yes

