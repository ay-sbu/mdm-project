FROM python:3.11.4-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . .

RUN chmod +x entrypoint.sh

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


ENTRYPOINT [ "sh", "./entrypoint.sh" ]