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
        user_agent = "yrele/1.0 jcberentsen@proton.me"
        headers = {"User-Agent": user_agent}
        response = self.m_http.get(yrl, headers=headers)

        if response.status_code < 400:
            # persist if we got a usable response
            extracted = response.text
            # TODO make an extract() function that picks out the information we are really interested in
            print(f"We got a successful response from yr. Sized {len(extracted)} for {location}")
            self.m_persistency.store_observation(location, extracted)
        else:
            print(f"We got a failure response from yr for {location}: {response.status_code}")

        return response
