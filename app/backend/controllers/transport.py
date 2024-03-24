from sqlalchemy.orm import Session
from sqlalchemy import func, cast, Float
from models import models, schemas


def get_transport_by_id(db: Session, transport_id: int):
    return db.query(models.Transport).filter(models.Transport.id == transport_id).first()


def get_transport_by_city(db: Session, city: str):
    return db.query(models.Transport).filter(models.Transport.city.ilike(city)).all()


def get_transport_all(db: Session):
    return db.query(models.Transport).all()

def find_transport(db: Session, city: str):
    fastest = db.query(models.Transport).filter(models.Transport.city.ilike(city)).order_by(cast(func.replace(models.Transport.duration, 'h', ''), Float)).first()

    most_economical= db.query(models.Transport).filter(models.Transport.city.ilike(city)).order_by(cast(func.replace(models.Transport.price_econ, 'R$', ''), Float)).first()

    return [
{
    "fastest": {
        "id": fastest.id,
        "name": fastest.name,
        "price_confort": fastest.price_confort,
        "price_econ": fastest.price_econ,
        "city": fastest.city,
        "duration": fastest.duration,
        "seat": fastest.seat,
        "bed": fastest.bed
    },
    "most_economical": {
        "id": most_economical.id,
        "name": most_economical.name,
        "price_confort": most_economical.price_confort,
        "price_econ": most_economical.price_econ,
        "city": most_economical.city,
        "duration": most_economical.duration,
        "seat": most_economical.seat,
        "bed": most_economical.bed
    }
}
]
    


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
