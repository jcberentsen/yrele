#!/usr/bin/env python3

import pytest

import client.yr_client as yr

# Thin duck typed mocks
class NotFoundHttp:
    def get(self, url):
        return {"status": 404}

@pytest.fixture
def yr_client_not_found():
    # Setup code goes here
    http = NotFoundHttp()
    baseUrl = "host.test"
    client = yr.YrClient(baseUrl, http)
    yield client
