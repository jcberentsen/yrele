#!/usr/bin/env python3

from src.service.location import Location, oslo

def test_wrong_url_not_found(yr_client_not_found):
    """if we have a wrong url, we'd expect 404"""
    client = yr_client_not_found
    response = client.fetch_location(oslo);
    assert response["status"] == 404
    # TODO verify that the client took note of the error, so we can potentially persist issues for future investigation

def test_we_can_get_yr_data_for_a_location(mock_yr_client):
    client = mock_yr_client
    response = client.fetch_location(oslo);
    assert response["status"] == 200
    assert response["body"] == '{"properties": {"timeseries": []} }'

# TODO check successful response
# TODO sanity check response so we don't persist garbage
# TODO Check that valid weather response gets persisted
# TODO Cache recent data for same location (check persistence)
