# Skin Cancer Atlas Backend

We require data to be downloaded. The following need to be added to a directory relative to this project called "data":
* [21031_Mel_stlearn.h5ad](https://downloads.gmllab.com/skin-cancer-atlas/21031_Mel_stlearn.h5ad) - 85.9 MB
* [23346-10SP_labeled_xenium.h5ad](https://downloads.gmllab.com/skin-cancer-atlas/23346-10SP_labeled_xenium.h5ad) - 6.3 MB
* [30037-07BR_labeled_xenium.h5ad](https://downloads.gmllab.com/skin-cancer-atlas/30037-07BR_labeled_xenium.h5ad) - 11.6 MB
* [48974_Mel_stlearn.h5ad](https://downloads.gmllab.com/skin-cancer-atlas/48974_Mel_stlearn.h5ad) - 114.1 MB
* [48974-2B_cutoff50_cosmx_clean.h5ad](https://downloads.gmllab.com/skin-cancer-atlas/48974-2B_cutoff50_cosmx_clean.h5ad) - 46.3 MB
* [6475-07FC_labeled_xenium.h5ad](https://downloads.gmllab.com/skin-cancer-atlas/6475-07FC_labeled_xenium.h5ad) - 5.5 MB
* [66487_Mel_stlearn.h5ad](https://downloads.gmllab.com/skin-cancer-atlas/66487_Mel_stlearn.h5ad) - 82.2 MB
* [66487-1A_cutoff50_cosmx_clean.h5ad](https://downloads.gmllab.com/skin-cancer-atlas/66487-1A_cutoff50_cosmx_clean.h5ad) - 5.4 MB
* [6747-085P_cutoff50_cosmx_clean.h5ad](https://downloads.gmllab.com/skin-cancer-atlas/6747-085P_cutoff50_cosmx_clean.h5ad) - 6.7 MB
* [6767_Mel_stlearn.h5ad](https://downloads.gmllab.com/skin-cancer-atlas/6767_Mel_stlearn.h5ad) - 62.6 MB
* [9474-06BR_labeled_xenium.h5ad](https://downloads.gmllab.com/skin-cancer-atlas/9474-06BR_labeled_xenium.h5ad) - 7.9 MB
* [98594-09PY_labeled_xenium.h5ad](https://downloads.gmllab.com/skin-cancer-atlas/98594-09PY_labeled_xenium.h5ad) - 10.4 MB
* [B18_BCC_cutoff50_cosmx_clean.h5ad](https://downloads.gmllab.com/skin-cancer-atlas/B18_BCC_cutoff50_cosmx_clean.h5ad) - 73.9 MB
* [B18_BCC_stlearn.h5ad](https://downloads.gmllab.com/skin-cancer-atlas/B18_BCC_stlearn.h5ad) - 84.1 MB
* [B18_SCC_cutoff50_cosmx_clean.h5ad](https://downloads.gmllab.com/skin-cancer-atlas/B18_SCC_cutoff50_cosmx_clean.h5ad) - 86.0 MB
* [B18_SCC_stlearn.h5ad](https://downloads.gmllab.com/skin-cancer-atlas/B18_SCC_stlearn.h5ad) - 64.5 MB
* [D12_cutoff50_cosmx_clean.h5ad](https://downloads.gmllab.com/skin-cancer-atlas/D12_cutoff50_cosmx_clean.h5ad) - 25.7 MB
* [E15_BCC_stlearn.h5ad](https://downloads.gmllab.com/skin-cancer-atlas/E15_BCC_stlearn.h5ad) - 59.0 MB
* [E15_SCC_stlearn.h5ad](https://downloads.gmllab.com/skin-cancer-atlas/E15_SCC_stlearn.h5ad) - 51.9 MB
* [F21_BCC_stlearn.h5ad](https://downloads.gmllab.com/skin-cancer-atlas/F21_BCC_stlearn.h5ad) - 62.0 MB
* [F21_SCC_stlearn.h5ad](https://downloads.gmllab.com/skin-cancer-atlas/F21_SCC_stlearn.h5ad) - 60.2 MB
* [P13_cutoff50_cosmx_clean.h5ad](https://downloads.gmllab.com/skin-cancer-atlas/P13_cutoff50_cosmx_clean.h5ad) - 14.2 MB
* [P30_cutoff50_cosmx_clean.h5ad](https://downloads.gmllab.com/skin-cancer-atlas/P30_cutoff50_cosmx_clean.h5ad) - 12.2 MB

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

Remove old installation:
```conda env remove --prefix [some-directory]/conda/skin-cancer-atlas-backend --y```

* Setup a conda environment:
  * ```conda create --prefix [some-directory]/conda/skin-cancer-atlas-backend python=3.11 -y```
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

* Running server locally:
  * ```docker build -f Dockerfile.local -t my-fastapi-lambda .```
  * ```docker run -p 8000:8000 my-fastapi-app```
* You will need to download the data and place it in the ./data directory.

* When deploying to production you can test it with (in the AWS console for example):
```json
{
  "resource": "/samples",
  "path": "/samples",
  "httpMethod": "GET",
  "headers": {
    "Accept": "application/json",
    "Content-Type": "application/json"
  },
  "requestContext": {
    "httpMethod": "GET"
  }
}
```

## Other Information

* Dockerfile - for deploying/testing in AWS Lambda,
* Dockerfile-local - for testing the Dockerfile locally.

Using:
* Python in Docker https://hub.docker.com/_/python  
* Debian https://www.debian.org/releases/

