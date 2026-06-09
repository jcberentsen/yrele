#!/usr/bin/env python3

import pytest

import client.yr_client as yr
import service.weather as service
from mocks import MockPersistency, NotFoundHttp, FoundHttp

@pytest.fixture
def yr_client_not_found():
    http = NotFoundHttp()
    client = yr.YrClient(http, None)
    yield client

@pytest.fixture
def mock_persistency():
    persistency = MockPersistency()
    yield persistency

@pytest.fixture
def mock_yr_client(mock_persistency):
    example = '{"properties": {"timeseries": []} }'
    http = FoundHttp(example)
    persistency = mock_persistency
    client = yr.YrClient(http, persistency)
    yield client

@pytest.fixture
def empty_service(mock_persistency):
    persistency = mock_persistency
    weather = service.Weather(persistency)
    yield weather
