#!/usr/bin/env python3
import uvicorn

def main():
    uvicorn.run("app:app", host="0.0.0.0", port=1876)

if __name__ == "__main__":
    main()
