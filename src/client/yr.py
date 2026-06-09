#!/usr/bin/env python3

import requests
import json

import src.client.yr_client as yr
from src.service.location import Location, oslo

def main():
    http = requests
    baseUrl = ""
    client = yr.YrClient(baseUrl, http)
    response = client.fetch_location(oslo)
    pretty = json.dumps(response.json(), indent=4, sort_keys=True)
    print(pretty)

    # print(r)

if __name__ == "__main__":
    main()
