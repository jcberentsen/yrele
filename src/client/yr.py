#!/usr/bin/env python3

import requests
import json

import src.client.yr_client as yr
from src.service.location import Location, oslo
from src.common.persist_sqlite import PersistencySqlite

def main():
    http = requests
    persistency = PersistencySqlite()
    client = yr.YrClient(http, persistency)
    response = client.fetch_location(oslo)
    pretty = json.dumps(response.json(), indent=4, sort_keys=True)
    print(pretty)

if __name__ == "__main__":
    main()
