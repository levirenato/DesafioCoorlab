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



@routes.get("/")
def read_transports(db: Session = Depends(get_db)):
    try:
        transports = transport.get_transport_all(get_db)
        return transports
    except:
        return {"erro":"erro"}
