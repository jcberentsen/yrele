#!/usr/bin/env python3

from fastapi import FastAPI, status
from pydantic import BaseModel, Field

from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastApi):
    db = None # TODO
    print("Yielding a db for use by handler")
    yield {"db": db}

    # TODO clean up db
    print("Cleaning up db pool...")

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def read_root():
    return {"status": "success", "message": "This is an api server for weather data (not a teapot). See /docs, /redoc, /openapi.json endpoints for details"}

@app.get("/locations")
async def read_locations():
    # TODO delegate to Persistence
    return {"locations": []}

@app.delete("/locations/{location_id}")
async def delete_locations(location_id: int):
    # TODO delegate to Persistence
    return {"locations": []}

@app.post("/locations")
async def create_location(location, status_code=status.HTTP_201_CREATED):
    # TODO delegate to Persistence
    fresh_location_id = 0
    example_location = {
        "name": "Oslo",
        "lat": 59.9139,
        "lon": 10.7522
        }
    return {"created": fresh_location_id, "locations": [example_location]}
