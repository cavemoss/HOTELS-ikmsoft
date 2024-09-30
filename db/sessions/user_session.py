from db.models import *
from db.create_db import create_session

session = create_session()


def get_all_devices(): return session.query(
    Devices.id, 
    Devices.room_number, 
    Devices.device_status
).all()

def get_all_news(): return session.query(
    MainNews.id, 
    MainNews.title, 
    MainNews.description, 
    MainNews.photos,
    MainNews.qr_url
).all()

def get_all_about(): return session.query(
    About.id, 
    About.title,
    About.description, 
    About.photos
).all()

def get_all_services(): return session.query(
    HotelServices.id, 
    HotelServices.name,
    HotelServices.description, 
    HotelServices.price, 
    HotelServices.photos
).all()

def get_all_categories(): return session.query(
    CityGuideCategories.id,
    CityGuideCategories.fk,
    CityGuideCategories.title, 
    CityGuideCategories.photos,
).all()

def get_all_guides(fk: str = None): return session.query(
    CityGuides.id, 
    CityGuides.placename, 
    CityGuides.description, 
    CityGuides.address, 
    CityGuides.recommended,
    CityGuides.photos,
    None if fk else CityGuides.category,
    CityGuides.qr_url
).filter((CityGuides.category==fk) if fk is not None else True)

def get_restaurant_menu(): return session.query(
    Restaurant.id, 
    Restaurant.name, 
    Restaurant.description, 
    Restaurant.price, 
    Restaurant.recommended,
    Restaurant.photos,
    Restaurant.qr_url
).all()

def get_all_recommendations():
    guides = session.query(
        CityGuides.id, 
        CityGuides.placename, 
        CityGuides.photos
    ).filter(CityGuides.recommended==True).all()

    restaurant = session.query(
        Restaurant.id, 
        Restaurant.name, 
        Restaurant.photos
    ).filter(Restaurant.recommended==True).all()

    return (
        [tuple(('guide',) + tuple(row)) for row in guides] + 
        [tuple(('menu',) + tuple(row)) for row in restaurant]
    )

def get_all_applications(): return session.query(
    Applications.id, 
    Applications.name, 
    Applications.resource_url, 
    Applications.photos
).all()
