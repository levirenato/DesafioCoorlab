from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

import uvicorn
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

@app.get("/")
async def get_all():
    
    return {"hello":"world"}

@app.get("/{city}")
async def serch(city):
    return {"hello":"world"}


if __name__ == '__main__':
    uvicorn.run("app:app", port=3000, reload=True)