FROM nvidia/cuda:12.1.0-runtime-ubuntu22.04

RUN apt-get update && apt-get install -y \
    curl \
    bash \
    wget

WORKDIR /app
COPY app.py .

CMD ["python", "app.py"]
