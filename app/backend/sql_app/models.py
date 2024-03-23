from sqlalchemy import String

from .database import Base


class User(Base):
    __tablename__ = "transport"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    price_confort = Column(String)
    price_econ = Column(String)
    city = Column(String)
    duration = Column(String)
    seat = Column(String)
    bed = Column(String)
    