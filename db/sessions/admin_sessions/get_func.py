from db.create_db import create_session
from db.models import *

session = create_session()

def get_device_by_id(id: int): return session.query(
    Devices.room_number,
    Devices.device_status
).filter(Devices.id==id).one_or_none()

def get_news_by_id(id: int): return session.query(
    MainNews.title, 
    MainNews.description, 
    MainNews.photos,
    MainNews.qr_url
).filter(MainNews.id==id).one_or_none()

def get_about_by_id(id: int): return session.query(
    About.title, 
    About.description, 
    About.photos
).filter(About.id==id).one_or_none()

def get_service_by_id(id: int): return session.query(
    HotelServices.name, 
    HotelServices.description, 
    HotelServices.price,
    HotelServices.photos
).filter(HotelServices.id==id).one_or_none()

def get_guide_by_id(id: int): return session.query(
    CityGuides.placename,
    CityGuides.description,
    CityGuides.address,
    CityGuides.photos,
    CityGuides.qr_url
).filter(CityGuides.id==id).one_or_none()

def get_restaurant_by_id(id: int): return session.query(
    Restaurant.name, 
    Restaurant.description, 
    Restaurant.price,
    Restaurant.photos,
    Restaurant.qr_url
).filter(Restaurant.id==id).one_or_none()

def get_application_by_id(id: int): return session.query(
    Applications.name,
    Applications.resource_url,
    Applications.photos
).filter(Applications.id==id).one_or_none()