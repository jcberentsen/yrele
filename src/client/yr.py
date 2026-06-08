#!/usr/bin/env python3

import requests
import urllib.parse

def locationQuery(lat, lon):
    data = {
        "lat": lat,
        "lon": lon
    }
    return urllib.parse.urlencode(data)

def main():
    query = locationQuery("59.9139", "10.7522")

    yrl = 'https://api.met.no/weatherapi/locationforecast/2.0/compact?' + query
    # yrl = "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={lat}&lon={lon}"
    r = requests.get(yrl)
    print(r)

if __name__ == "__main__":
    main()
