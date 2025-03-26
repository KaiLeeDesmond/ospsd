# main.py

from fastapi import FastAPI
from pydantic import BaseModel
from src.component import OSPSD
from flask import Flask, render_template, request, jsonify
import os, re, datetime
import db
from models import Book



app = FastAPI()

ospd = OSPSD()

class Data(BaseModel):
    """Model for data to be processed."""
    data: dict

@app.post("/process_data")
def process_data(data: Data):
    """Process data using OSPSD."""
    processed_data = ospd.process_data(data.data)
    return {"processed": processed_data}

@app.get("/get_results")
def get_results():
    """Retrieve results from OSPSD processing."""
    results = ospd.get_results()
    return {"results": results}

@app.get("/")
def root():
    """Root endpoint for testing."""
    return {"message":"Hello World"}
