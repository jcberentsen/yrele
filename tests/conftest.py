#!/usr/bin/env python3

import pytest

import client.yr_client as yr
import service.weather as service
from mocks import MockPersistency, NotFoundHttp

@pytest.fixture
def yr_client_not_found():
    http = NotFoundHttp()
    baseUrl = "host.test"
    client = yr.YrClient(baseUrl, http)
    yield client

@pytest.fixture
def empty_service():
    persistency = MockPersistency()
    weather = service.Weather(persistency)
    yield weather
