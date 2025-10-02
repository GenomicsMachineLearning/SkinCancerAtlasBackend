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

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

# Lambda runtime interface client
RUN pip install awslambdaric

# Copy application code
COPY app/ ./app/
COPY lambda_handler.py .

ENTRYPOINT ["/usr/local/bin/python", "-m", "awslambdaric"]
CMD ["lambda_handler.lambda_handler"]
