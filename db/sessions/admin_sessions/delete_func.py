from db.create_db import create_session
from db.models import *

session = create_session()

def delete_device(id: int) -> None:
    session.delete(session.query(Devices).filter(Devices.id == id).scalar())
    session.commit()

def delete_news(id: int) -> None:
    session.delete(session.query(MainNews).filter(MainNews.id == id).scalar())
    session.commit()

def delete_about(id: int) -> None:
    session.delete(session.query(About).filter(About.id == id).scalar())
    session.commit()

def delete_service(id: int) -> None:
    session.delete(session.query(HotelServices).filter(HotelServices.id == id).scalar())
    session.commit()

def delete_category(id: int) -> None:
    fk = session.query(CityGuideCategories.fk).filter(CityGuideCategories.id == id)
    session.query(CityGuides).filter(CityGuides.category == fk).delete()
    session.delete(session.query(CityGuideCategories).filter(CityGuideCategories.id == id).scalar())
    session.commit()

def delete_guide(id: int) -> None:
    session.delete(session.query(CityGuides).filter(CityGuides.id == id).scalar())
    session.commit()

def delete_menu(id: int) -> None:
    session.delete(session.query(Restaurant).filter(Restaurant.id == id).scalar())
    session.commit()

def delete_app(id: int) -> None:    
    session.delete(session.query(Applications).filter(Applications.id == id).scalar())
    session.commit()