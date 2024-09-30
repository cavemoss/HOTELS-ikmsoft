from db.create_db import create_session
from db.models import *

session = create_session()

device_status = {
    'ONLINE' : DeviceStatus.ONLINE,
    'OFFLINE' : DeviceStatus.OFFLINE,
    'STANDBY' : DeviceStatus.STANDBY,
    'MALFUNCTION' : DeviceStatus.MALFUNCTION
}

def add_device(room_number: int, device_status_str: str) -> None:
    session.add(Devices(
        room_number=room_number,
        device_status=device_status[device_status_str]
    ))
    session.commit()

def add_news(title: str, description: str, photos: list, qr_url: str) -> None:
    session.add(MainNews(
        title=title,
        description=description,
        photos=photos,
        qr_url=qr_url
    ))
    session.commit()

def add_about(title: str, description: str, photos: list) -> None:
    session.add(About(
        title=title,
        description=description,
        photos=photos
    ))
    session.commit()

def add_service(name: str, description: str, price: int, photos: list) -> None:
    session.add(HotelServices(
        name=name, 
        description=description, 
        price=price, 
        photos=photos
    ))
    session.commit()

def add_guide_category(title: str, photos: list) -> None:
    session.add(CityGuideCategories(
        fk=title,
        title=title, 
        photos=photos
    ))
    session.commit()

def add_guide(placename: str, description: str, address: str, category: str, recommended: bool, photos: list, qr_url: str) -> None:
    session.add(CityGuides(
        placename=placename, 
        description=description, 
        address=address, 
        category=category, 
        recommended=recommended, 
        photos=photos,
        qr_url=qr_url
    ))
    session.commit()

def add_menu(name: str, description: str, price: int, recommended: bool, photos: list, qr_url: str) -> None:
    session.add(Restaurant(
        name=name, 
        description=description, 
        price=price, 
        recommended=recommended,
        photos=photos,
        qr_url=qr_url
    ))
    session.commit()

def add_app(name: str, resource_url: str, photos: list) -> None:
    session.add(Applications(
        name=name,
        resource_url=resource_url,
        photos=photos
    ))
    session.commit()

def check_category(title:str):
    if len(session.query(CityGuideCategories.fk).filter(CityGuideCategories.fk==title).all()) != 0: return False
    return True
