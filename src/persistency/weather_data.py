#!/usr/bin/env python3

import sqlite3

def main():
    con = sqlite3.connect("localweather.db")
    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS user (id, name)")
        cur.execute("CREATE TABLE IF NOT EXISTS userlocations (userid, locationid)")
        cur.execute("CREATE TABLE IF NOT EXISTS locations (locationid, lat, lon)")
        cur.execute("CREATE TABLE IF NOT EXISTS weather (locationid, timestamp, report)")

        # check tables
        res = cur.execute("SELECT name FROM sqlite_master")
        print(res.fetchall())

if __name__ == "__main__":
    main()
