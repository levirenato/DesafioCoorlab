from sqlalchemy import Column, String, Integer

from database.database import Base


class Transport(Base):
    __tablename__ = "transport"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    price_confort = Column(String)
    price_econ = Column(String)
    city = Column(String)
    duration = Column(String)
    seat = Column(String)
    bed = Column(String)
    