# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

USER 10000:10000

ENTRYPOINT ["python", "bot.py"]
