#!/usr/bin/env python3

import pytest

import client.yr_client as yr
import service.weather as service

# Thin duck typed mocks
class NotFoundHttp:
    def get(self, url):
        return {"status": 404}

@pytest.fixture
def yr_client_not_found():
    http = NotFoundHttp()
    baseUrl = "host.test"
    client = yr.YrClient(baseUrl, http)
    yield client

class MockPersistency:
    def __init__(self):
        self.locations = {}
        self.fresh_location_id = 0

    def list_locations(self):
        return self.locations.values()

    def delete_location(self, location_id):
        self.locations.delete(location_id)
        return self.list_locations()

    def add_location(self, location):
        location_id = self.fresh_location_id
        self.locations[location_id] = location
        self.fresh_location_id += 1
        return {"created": location_id, "locations": self.list_locations()}

@pytest.fixture
def empty_service():
    persistency = MockPersistency()
    weather = service.Weather(persistency)
    yield weather
