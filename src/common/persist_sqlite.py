#!/usr/bin/env python3

import sqlite3

class PersistencySqlite:
    def __init__(self):
        self.con = sqlite3.connect("localweather.db")
        cursor = self.con.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS locations (locationid INTEGER PRIMARY KEY, lat, lon)")
        cursor.execute("CREATE TABLE IF NOT EXISTS weather (locationid, timestamp, report)")

        # check tables
        cursor.execute("SELECT name FROM sqlite_master")
        print(cursor.fetchall())

    def list_locations(self):
        cursor = self.con.cursor()
        cursor.execute("SELECT * FROM locations")
        items = cursor.fetchall()
        print(items)
        return list(items) # TODO transform to Location values

    def commit(self):
        self.con.commit()

    def delete_location(self, location_id):
        cursor = self.con.cursor()
        cursor.execute("DELETE FROM locations WHERE locationid=?", (location_id,))
        self.commit()
        return self.list_locations()

    def add_location(self, location):
        cursor = self.con.cursor()
        cursor.execute("INSERT INTO locations (lat,lon) VALUES (?,?)", (location.lat, location.lon,))
        location_id = cursor.lastrowid
        self.commit()
        return {"created": location_id, "locations": self.list_locations()}

    def store_observation(location, weather_data):
        # TODO
        pass
