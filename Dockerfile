FROM python:3.8
ADD . /src
WORKDIR /src
RUN pip install -r requirements-dev.txt