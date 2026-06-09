#!/usr/bin/env python3

from service.location import oslo, kongsvinger

def test_service_uses_persistency(empty_service):
    """The service can respond with data from persistency"""
    service = empty_service
    locations = service.list_locations();
    assert len(locations) == 0

def test_we_can_add_a_location(empty_service):
    service = empty_service
    location = oslo

    location_id = service.add_location(oslo)
    locations = service.list_locations();
    assert len(locations) == 1

def test_we_can_add_two_different_locations(empty_service):
    service = empty_service
    location_id = service.add_location(oslo)
    location_id = service.add_location(kongsvinger)
    locations = service.list_locations();
    assert len(locations) == 2
