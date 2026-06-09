#!/usr/bin/env python3

class PersistencySqlite:
    def __init__(self):
        pass

    def list_locations(self):
        # TODO
        return []

    def delete_location(self, location_id):
        # TODO
        return self.list_locations()

    def add_location(self, location):
        # TODO
        location_id = 0 # TODO use sql for allocating location id
        return {"created": location_id, "locations": self.list_locations()}

    def store_observation(location, weather_data):
        pass
