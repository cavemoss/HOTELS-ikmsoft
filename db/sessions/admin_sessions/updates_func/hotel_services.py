from db.create_db import create_session
from db.models import HotelServices

session = create_session()

def name(id: int, name:str):
    OBJ = session.query(HotelServices).filter(HotelServices.id == id).scalar()
    OBJ.name = name
    session.commit()

def description(id: int, description:str):
    OBJ = session.query(HotelServices).filter(HotelServices.id == id).scalar()
    OBJ.description = description
    session.commit()

def price(id: int, price:int):
    OBJ = session.query(HotelServices).filter(HotelServices.id == id).scalar()
    OBJ.price = price
    session.commit()

def photos(id: int, photos: list):
    OBJ = session.query(HotelServices).filter(HotelServices.id == id).scalar()
    OBJ.photos = photos
    session.commit()
