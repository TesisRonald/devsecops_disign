FROM python:3.8-alpine
RUN pip install --upgrade setuptools==65.5.1

WORKDIR /app
# RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev cargo
COPY ./requirements.txt .
COPY ./product .
RUN pip install -r requirements.txt
