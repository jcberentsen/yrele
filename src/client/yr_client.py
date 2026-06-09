#!/usr/bin/env python3

import urllib.parse

# TODO move Location to common module
from src.service.location import Location

def locationQuery(location: Location):
    data = {
        "lat": location.lat,
        "lon": location.lon
    }
    return urllib.parse.urlencode(data)

class YrClient:
    def __init__(self, baseUrl, http):
        self.m_http = http;
        self.m_baseUrl = baseUrl

    def fetch_location(self, location: Location):
        query = locationQuery(location)
        yrl = 'https://api.met.no/weatherapi/locationforecast/2.0/compact?' + query
        response = self.m_http.get(yrl)

        # TODO persist if we got a usable response
        return response
