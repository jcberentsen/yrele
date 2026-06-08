#!/usr/bin/env python3

def test_service_uses_persistency(empty_service):
    """The service can respond with data from persistency"""
    service = empty_service
    user = "user"
    locations = service.listLocations(user);
    assert len(locations) == 0
