from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

from routes import transport



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


# Routes
app.include_router(transport.routes, prefix='')

if __name__ == '__main__':
    uvicorn.run("run:app", port=3000, reload=True)