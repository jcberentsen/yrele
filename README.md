# YRele - a simple relay for some YR weather data


# Platform requirements

* git
* python >= 3.14
* docker (colima)
* docker-compose

# Get started - Macos

## clone repo

``` sh
git clone https://github.com/jcberentsen/yrele.git
```

## install python if necessary
``` sh
brew install python
❯ python3.14 --version
Python 3.14.5

❯ python3 -m venv venv
❯ source venv/bin/activate
on  main [!] via 🐍 v3.14.5 (venv)
❯
pip install -r requirements.txt
```

# Run pytests

Run all python core, client and service tests

``` sh
python -m pytest
# or
pytest
```

# Test the real http client on the command line (local db)

This should successfully complete a weather request for the Oslo location

``` sh
python -m src.client.yr
```

# Run the real http weather server on the command line (local db)
(Uses uvicorn)
``` sh
# from python using uvicorn module
python src/server/weather_server.py
# or uvicorn middleware
uvicorn src.server.app:app --port 1876 --reload
# or using docker-compose
docker-compose up --build
```

# Test with browser
[localhost](http://localhost:1876/)
``` sh
open "localhost:1876"
```

# inspect the fastapi docs
[local docs](http://localhost:1876/docs)
[openapi json](http://localhost:1876/openapi.json)
[local docs redoc style](http://localhost:1876/redoc)

# Database introspection
``` sh
> python -m src.persistency.weather_data
[('user',), ('userlocations',), ('locations',), ('weather',)]
```

# Build docker images
Dockerfile for server

# Run docker compose
docker compose for volume mounting persistent (local) database
``` sh
docker-compose up --build
# This should start the docker container uvicorn webserver with the current folder volume-mounted
```

# CI Github actions
TODO smoketest with docker compose and pytest

# Chores
Freeze updated requirements

``` sh
pip freeze > requirements.txt
```
