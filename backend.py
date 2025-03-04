# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 09:49:39 2025

@author: cpaji
"""
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from any frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/add")
def add(a: float, b: float):
    return {"result": a + b}

@app.get("/subtract")
def subtract(a: float, b: float):
    return {"result": a - b}

@app.get("/multiply")
def multiply(a: float, b: float):
    return {"result": a * b}

@app.get("/divide")
def divide(a: float, b: float):
    if b == 0:
        return {"error": "Division by zero is not allowed"}
    return {"result": a / b}
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

