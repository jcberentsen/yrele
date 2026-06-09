#!/usr/bin/env python3

import sqlite3

class PersistencySqlite:
    def __init__(self):
        self.con = sqlite3.connect("localweather.db")
        cur = self.con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS locations (locationid INTEGER PRIMARY KEY, lat, lon)")
        cur.execute("CREATE TABLE IF NOT EXISTS weather (locationid, timestamp, report)")

        # check tables
        res = cur.execute("SELECT name FROM sqlite_master")
        print(res.fetchall())

    def list_locations(self):
        # TODO
        return []

    def delete_location(self, location_id):
        # TODO
        return self.list_locations()

    def add_location(self, location):
        cursor = self.con.cursor()
        cursor.execute("INSERT INTO locations (lat,lon) VALUES (?)", (location.lat, location.lon,))
        location_id = cursor.lastrowid
        return {"created": location_id, "locations": self.list_locations()}

    def store_observation(location, weather_data):
        pass
