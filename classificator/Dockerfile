FROM python:3.12-alpine AS base

RUN apk update \
    && apk upgrade \
    && apk add --no-cache curl git build-base \
    && rm -rf /var/cache/apk/*

WORKDIR /home/app

COPY common/ ./common

COPY classificator/ ./classificator
COPY .env ./

RUN pip install --no-cache-dir -r classificator/requirements.txt

CMD ["uvicorn", "classificator.src.app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]