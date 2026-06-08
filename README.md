# YRele - a simple relay for some YR weather data


# Platform requirements
python >= 3.14

# Get started - Macos

``` sh
brew install python
...
❯ python3.14 --version
Python 3.14.5

❯ python3 -m venv venv
❯ source venv/bin/activate
ssb-case on  main [!] via 🐍 v3.14.5 (venv)
❯
```

# Run pytests

Run all python core, client and service tests

``` sh
pytest
```

# Test the real http client on the command line (local db)
``` sh
python src/client/yr.py
```

# run the real http weather server on the command line (local db)
``` sh
python src/server/weather_server.py
```

# Build docker images
TODO

# Run docker compose
TODO

# Test with browser

``` sh
open "localhost:1876"
```
