FROM rackspacedot/python37
MAINTAINER Nerd-Bear "python@istruly.sexy"

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

WORKDIR /app/server
EXPOSE 80
CMD python3 main.py