# Skin Cancer Atlas Backend

We require data to be downloaded. The following need to be added to a directory relative to this project called "data":
* [xxx.h5ad](https://downloads.gmllab.com/skin-cancer-atlas/xxx.h5ad) - 40.8 MB

## Running Locally

We have two methods for running the backend server:
* Run in a conda environment or
* Docker.

### Running the Server in a Local Python Environment

The steps to run in a local conda environment include:
* Setup a new Python environment and install dependencies.
* Setup local database.
* Run server.

We assume you already have conda installed.

* Setup a conda environment:
  * ```conda create create --prefix [some-directory]/conda/skin-cancer-atlas-backend python=3.10 -y```
* Activate conda environment:
  * ```conda activate [some-directory]/conda/skin-cancer-atlas-backend```

* Install Python dependencies:
  * ```python -m pip install --use-pep517 -r requirements-dev.txt```

* Run server:
  * ```uvicorn app.main:app --reload --host 0.0.0.0 --port 8000```

* Test server (make sure you have downloaded xxxx.h5ad and put into the ./data directory):

### Running the Server using Docker

* Install Docker
  * https://docs.docker.com/desktop/install/mac-install/
  * https://docs.docker.com/desktop/install/windows-install/
  * Add ```$HOME/.docker/bin``` to you PATH.

* Running server:
  * ```docker build -f Dockerfile.local -t my-fastapi-lambda .```
  * ```docker run --rm -p 9000:8080 my-fastapi-lambda```

* Send a test request:
```commandline
curl -X POST "http://localhost:9000/2015-03-31/functions/function/invocations" \
  -H "Content-Type: application/json" \
  -d '{
  "resource": "/samples",
  "path": "/samples",
  "httpMethod": "GET",
  "headers": {
    "Accept": "application/json",
    "Host": "localhost"
  },
  "requestContext": {}
}'
```

## Other Information

* Dockerfile - for deploying/testing in AWS Lambda,
* Dockerfile-local - for testing the Dockerfile locally.

Using:
* Python in Docker https://hub.docker.com/_/python  
* Debian https://www.debian.org/releases/

