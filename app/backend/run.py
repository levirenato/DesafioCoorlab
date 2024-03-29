from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

from routes import Transport



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
app.include_router(Transport.routes, prefix='')

if __name__ == '__main__':
    uvicorn.run("run:app", port=3000, reload=True)