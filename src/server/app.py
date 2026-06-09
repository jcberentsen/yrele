#!/usr/bin/env python3

from fastapi import FastAPI, status, Request, Depends

from contextlib import asynccontextmanager

import src.service.weather as service
from src.service.location import Location
from src.service.weather import Weather

from src.common.persist_sqlite import PersistencySqlite

@asynccontextmanager
async def lifespan(app: FastAPI):
    persistency = PersistencySqlite()
    weather = service.Weather(persistency)
    print("Yielding weather service from persistency")
    app.state.service = weather
    yield {"service": weather}

    # TODO clean up
    print("Cleaning up weather service context...")

app = FastAPI(lifespan=lifespan)

def get_weather_service(request: Request):
    print(request.app.state)
    return request.app.state.service

@app.get("/")
async def read_root():
    return {"status": "success", "message": "This is an api server for weather data (not a teapot). See /docs, /redoc, /openapi.json endpoints for details"}

@app.get("/locations")
async def read_locations(weather: Weather = Depends(get_weather_service)):
    return {"locations": weather.list_locations()}

@app.delete("/locations/{location_id}")
async def delete_location(location_id: int, weather: Weather = Depends(get_weather_service)):
    return weather.delete_location(location_id)

@app.post("/locations")
async def create_location(location : Location, status_code=status.HTTP_201_CREATED, weather: Weather = Depends(get_weather_service)):
    return weather.add_location(location)
