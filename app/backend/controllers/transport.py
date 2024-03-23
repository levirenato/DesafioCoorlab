from sqlalchemy.orm import Session

from models import models, schemas


def get_transport_by_id(db: Session, user_id: int):
    return db.query(models.Transport).filter(models.Transport.id == user_id).first()


def get_transport_by_city(db: Session, city: str):
    return db.query(models.Transport).filter(models.Transport.city == city).all()


def get_transport_all(db: Session):
    return db.query(models.Transport).all()


def create_transport(db: Session, transport: schemas.TransportCreate):
    db_transport = models.Transport(
        name = transport.name,
        price_confort= transport.price_confort,
        price_econ= transport.price_econ,
        city= transport.city,
        duration= transport.duration,
        seat= transport.seat,
        bed= transport.bed,
    )
    db.add(db_transport)
    db.commit()
    db.refresh(db_transport)
    
    return db_transport
