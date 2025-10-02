FROM public.ecr.aws/docker/library/python:3.10-slim-bookworm

RUN apt-get update && apt-get install -y \
    build-essential \
    libhdf5-dev \
    ca-certificates \
    curl \
    git \
    gzip \
    pkg-config \
    procps \
    tar \
    unzip \
    wget \
    zlib1g \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /var/task
COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.8.3 /lambda-adapter /opt/extensions/lambda-adapter

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./app/

ENV AWS_LWA_INVOKE_MODE=response_stream
ENV AWS_LWA_PORT=8000

# Use uvicorn to serve FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]