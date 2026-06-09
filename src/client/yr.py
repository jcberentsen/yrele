#!/usr/bin/env python3

import requests
import urllib.parse

from src.service.location import Location, oslo

def locationQuery(location: Location):
    data = {
        "lat": location.lat,
        "lon": location.lon
    }
    return urllib.parse.urlencode(data)

def main():
    query = locationQuery(oslo)

    yrl = 'https://api.met.no/weatherapi/locationforecast/2.0/compact?' + query
    r = requests.get(yrl)
    print(r.json())

    # print(r)

if __name__ == "__main__":
    main()
