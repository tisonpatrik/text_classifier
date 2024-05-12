FROM python:3.12-alpine AS base

RUN apk update \
    && apk upgrade \
    && apk add --no-cache curl git build-base \
    && rm -rf /var/cache/apk/*

# Setting the working directory in the container
WORKDIR /home/app

COPY common/ ./common

COPY openai_solution/ ./openai_solution
COPY .env ./

RUN pip install --no-cache-dir -r openai_solution/requirements.txt

CMD ["uvicorn", "openai_solution.src.app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
