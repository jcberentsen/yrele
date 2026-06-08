#!/usr/bin/env python3

import client.yr_client as yr

# Thin duck typed mocks
class NotFoundHttp:
    def get(self, url):
        return {"status": 404}

# Test suite
class TestClient:
    """The YrClient should behave predictably"""
    def test_wrong_url_not_found(self):
        """if we have a wrong url, we'd expect 404"""
        http = NotFoundHttp()
        client = yr.YrClient(http)

        url = "wrong"
        response = client.update(url);
        assert response["status"] == 404
        # TODO verify that the client took note of the error, so we can potentially persist issues for future investigation

# TODO check successful response
# TODO sanity check response so we don't persist garbage
# TODO Check that valid weather response gets persisted
# TODO Cache recent data for same location (check persistence)
