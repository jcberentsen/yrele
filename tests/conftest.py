#!/usr/bin/env python3

import pytest

import client.yr_client as yr
import service.weather as service
from mocks import MockPersistency, NotFoundHttp, FoundHttp

@pytest.fixture
def yr_client_not_found():
    http = NotFoundHttp()
    client = yr.YrClient(http)
    yield client

@pytest.fixture
def mock_yr_client():
    example = '{"properties": {"timeseries": []} }'
    http = FoundHttp(example)
    client = yr.YrClient(http)
    yield client

@pytest.fixture
def empty_service():
    persistency = MockPersistency()
    weather = service.Weather(persistency)
    yield weather
