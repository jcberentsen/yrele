#!/usr/bin/env python3

from pydantic import BaseModel, Field

class Location(BaseModel):
    id: int
    name: str = "oslo"
    lat: str = "59.913"
    lon: str = "10.7522"

oslo: Location = Location(
    id = 0,
    name="Oslo",
    lat="59.9139",
    lon="10.7522",
)

kongsvinger: Location = Location(
    id = 1,
    name="Kongsvinger",
    lat="60.1898",
    lon="11.9901",
)
