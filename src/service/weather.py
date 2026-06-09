#!/usr/bin/env python3

class Weather:
    def __init__(self, persistency):
        self.persistency = persistency

    def list_locations(self):
        return self.persistency.list_locations()

    def delete_location(location_id):
        return {"locations": []}

    def add_location(location):
        location_id = 0
        return {"created": location_id, "locations": [location]}
