#!/usr/bin/env python3

def test_wrong_url_not_found(yr_client_not_found):
    """if we have a wrong url, we'd expect 404"""
    client = yr_client_not_found
    response = client.update();
    assert response["status"] == 404
    # TODO verify that the client took note of the error, so we can potentially persist issues for future investigation

# TODO check successful response
# TODO sanity check response so we don't persist garbage
# TODO Check that valid weather response gets persisted
# TODO Cache recent data for same location (check persistence)
