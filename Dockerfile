FROM rackspacedot/python37
MAINTAINER Nerd-Bear "python@istruly.sexy"

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential psycopg2 libpq-dev

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt


EXPOSE 80
CMD python3 server/main.py