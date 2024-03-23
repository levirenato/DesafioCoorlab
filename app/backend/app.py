from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

import json

app = FastAPI()

# CORS 
origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# methods

file = open('../../app/data.json')
DATA = json.load(file)["transport"]

@app.get("/")
async def get_all():
    
    return DATA

@app.get("/destiny/{city}")
async def serch(city):
    return DATA
