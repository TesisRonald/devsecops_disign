FROM python:3.8-alpine
# Crear un nuevo usuario no privilegiado
RUN adduser -D myuser

# Cambiar al nuevo usuario
USER myuser

WORKDIR /app
# RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev cargo
COPY ./requirements.txt .
COPY ./product .
RUN pip install -r requirements.txt
RUN pip uninstall -y setuptools
RUN pip install setuptools==68
RUN pip show setuptools
