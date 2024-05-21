FROM pytorch/pytorch:2.3.0-cuda12.1-cudnn8-runtime AS base

WORKDIR /home/app

COPY common/ ./common
COPY classificator/ ./classificator
COPY .env ./

RUN apt-get update && apt-get install -y \
    curl \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r classificator/requirements.txt

CMD ["uvicorn", "classificator.src.app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
