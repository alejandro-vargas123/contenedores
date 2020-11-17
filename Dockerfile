FROM python:latest

WORKDIR /src

ADD . /src

CMD [ "python", "main.py" ]
