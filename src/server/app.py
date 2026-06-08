#!/usr/bin/env python3

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"status": "success", "message": "Welcome to a modern Python HTTP server"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}
