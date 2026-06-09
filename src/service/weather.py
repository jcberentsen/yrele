#!/usr/bin/env python3

class Weather:
    def __init__(self, persistency):
        self.persistency = persistency

    def list_locations(self):
        return self.persistency.list_locations()
