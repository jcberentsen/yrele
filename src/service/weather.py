#!/usr/bin/env python3

class Weather:
    def __init__(self, persistency):
        self.persistency = persistency

    def listLocations(self, user):
        return self.persistency.listLocations(user)
