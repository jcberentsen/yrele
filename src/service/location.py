#!/usr/bin/env python3

from pydantic import BaseModel

class Location(BaseModel):
    name: str
    lat: float
    lon: float

oslo : Location = {
        "name": "Oslo",
        "lat": 59.9139,
        "lon": 10.7522
        }


kongsvinger : Location = {
        "name": "Kongsvinger",
        "lat": 60.1898,
        "lon": 11.9901
        }
