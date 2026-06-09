#!/usr/bin/env python3

from pydantic import BaseModel, Field

class Location(BaseModel):
    name: str = "oslo"
    lat: str = "59.913"
    lon: str = "10.7522"

oslo : Location = {
        "name": "Oslo",
        "lat": "59.9139",
        "lon": "10.7522"
        }

kongsvinger : Location = {
        "name": "Kongsvinger",
        "lat": "60.1898",
        "lon": "11.9901"
        }
