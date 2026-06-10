#!/usr/bin/env python3

class Weather:
    def __init__(self, persistency, yr):
        self.persistency = persistency
        self.yr = yr

    def list_locations(self):
        return self.persistency.list_locations()

    def delete_location(self, location_id):
        return self.persistency.delete_location(location_id)

    def add_location(self, location):
        return self.persistency.add_location(location)

    def fetch(self):
        locations = self.persistency.list_locations()
        fetches = list(map(self.yr.fetch_location, locations))
        # TODO consider failed fetches
        return len(fetches)
