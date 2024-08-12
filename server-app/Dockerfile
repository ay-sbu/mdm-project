FROM python:3.11.4-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# just for DEBUG with Dockerfile
ENV DEBUG=1
ENV SECRET_KEY=abbas
ENV ALLOWED_HOSTS=localhost,127.0.0.1

COPY . .

RUN chmod +x entrypoint.sh

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


ENTRYPOINT [ "sh", "./entrypoint.sh" ]