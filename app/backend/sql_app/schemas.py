from pydantic import BaseModel


class TransportBase(BaseModel):
    name: str
    price_confort: str
    price_econ: str
    city: str
    duration: str
    seat: str
    bed: str


class TransportCreate(TransportBase):
    pass


class Transport(TransportBase):
    id: int
    name: str
    price_confort: str
    price_econ: str
    city: str
    duration: str
    seat: str
    bed: str

    class Config:
        orm_mode = True