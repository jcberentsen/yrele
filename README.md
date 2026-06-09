# YRele - a simple relay for some YR weather data


# Platform requirements
python >= 3.14

# Get started - Macos

``` sh
brew install python
❯ python3.14 --version
Python 3.14.5

❯ python3 -m venv venv
❯ source venv/bin/activate
ssb-case on  main [!] via 🐍 v3.14.5 (venv)
❯
pip install -r requirements.txt
```

# Run pytests

Run all python core, client and service tests

``` sh
pytest
```

# Test the real http client on the command line (local db)

This should successfully complete a weather request for the Oslo location

``` sh
python src/client/yr.py
```

# run the real http weather server on the command line (local db)
(Uses uvicorn)
``` sh
python src/server/weather_server.py
```

# Database introspection
``` sh
> python src/persistency/weather_data.py
[('user',), ('userlocations',), ('locations',), ('weather',)]
```

# Build docker images
Dockerfile for server

# Run docker compose
docker compose for volume mounting persistent (local) database

# Test with browser
http://127.0.0.1:1876/

``` sh
open "localhost:1876"
```

# CI Github actions
TODO smoketest with docker compose and pytest
