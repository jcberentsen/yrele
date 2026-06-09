#!/usr/bin/env python3

# Thin duck typed mocks
class NotFoundHttp:
    def get(self, url):
        return {"status": 404}

class FoundHttp:
    def __init__(self, response_body):
        self.response_body = response_body

    def get(self, url):
        return {"status": 200, "body": self.response_body}

class MockPersistency:
    def __init__(self):
        self.locations = {}
        self.fresh_location_id = 0

    def list_locations(self):
        return self.locations.values()

    def delete_location(self, location_id):
        self.locations.delete(location_id)
        return self.list_locations()

    def add_location(self, location):
        location_id = self.fresh_location_id
        self.locations[location_id] = location
        self.fresh_location_id += 1
        return {"created": location_id, "locations": self.list_locations()}
