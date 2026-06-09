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
    def __init__(self, http, persistency):
        self.m_http = http;
        self.m_persistency = persistency;

    def fetch_location(self, location: Location):
        query = locationQuery(location)
        yrl = 'https://api.met.no/weatherapi/locationforecast/2.0/compact?' + query
        response = self.m_http.get(yrl)

        if response.status_code < 400:
            # persist if we got a usable response
            extracted = response.text # consider json()
            # TODO make an extract() function that picks out the information we are really interested in
            self.m_persistency.store_observation(location, extracted)
        return response
