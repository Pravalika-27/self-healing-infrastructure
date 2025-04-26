FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y ansible sshpass && rm -rf /var/lib/apt/lists/*
RUN pip install flask prometheus_client

COPY . /app

CMD ["python", "webhook.py"]
