#!/usr/bin/env python3

import sqlite3

from src.service.location import Location

def toLocation(tupled):
    return Location(id=tupled[0], name=tupled[1], lat= tupled[2], lon= tupled[3])

class PersistencySqlite:
    def __init__(self):
        self.con = sqlite3.connect("localweather.db")
        cursor = self.con.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS locations (name, lat, lon)")
        cursor.execute("CREATE TABLE IF NOT EXISTS weather (locationid, timestamp TEXT DEFAULT CURRENT_TIMESTAMP, report)")

        # check tables
        cursor.execute("SELECT name FROM sqlite_master")
        print(cursor.fetchall())

    def add_location(self, location):
        cursor = self.con.cursor()
        cursor.execute("INSERT INTO locations (name, lat,lon) VALUES (?,?,?)", (location.name, location.lat, location.lon,))
        location_id = cursor.lastrowid
        self.commit()
        return {"created": location_id, "locations": self.list_locations()}

    def list_locations(self):
        cursor = self.con.cursor()
        cursor.execute("SELECT rowid, * FROM locations")
        items = cursor.fetchall()
        locations = list(map(toLocation, items))
        print(locations)
        return locations

    def commit(self):
        self.con.commit()

    def delete_location(self, location_id):
        cursor = self.con.cursor()
        cursor.execute("DELETE FROM locations WHERE rowid=?", (location_id,))
        self.commit()
        return self.list_locations()


    def store_observation(self, location, weather_data):
        cursor = self.con.cursor()
        cursor.execute("INSERT INTO weather (locationid, report) VALUES (?,?)", (location.id, weather_data,))
        self.commit()
