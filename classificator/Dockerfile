FROM nvcr.io/nvidia/pytorch:24.04-py3 AS base

RUN apt-get update && apt-get install -y \
    curl \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /home/app

COPY common/ ./common
COPY labels/ ./labels

COPY classificator/ ./classificator
COPY .env ./

RUN pip install --no-cache-dir -r classificator/requirements.txt

CMD ["uvicorn", "classificator.src.app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
