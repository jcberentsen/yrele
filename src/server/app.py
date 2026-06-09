#!/usr/bin/env python3

from fastapi import FastAPI
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
    return {"status": "success", "message": "This is an api server for weather data (not a teapot)"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}
