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


class EmptyPersistency:
    def listLocations(self, user):
        return []

@pytest.fixture
def empty_service():
    persistency = EmptyPersistency()
    weather = service.Weather(persistency)
    yield weather
