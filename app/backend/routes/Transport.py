from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from controllers import transport
from models import models, schemas
from database.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

routes = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@routes.get("/", response_model=list[schemas.Transport])
def read_transports(Session = Depends(get_db)):
    return transport.get_transport_all(Session)


@routes.get("/{city}", response_model=list[schemas.Transport])
def read_transports_by_city(city:str,Session = Depends(get_db)):
    return transport.get_transport_by_city(Session, city)

@routes.get("/search/{city}")
def find_bestest(city:str,Session = Depends(get_db)):
    return transport.find_transport(Session, city)