from db.create_db import create_session
from db.models import CityGuideCategories

session = create_session()

def title(id: int, title:str):
    OBJ = session.query(CityGuideCategories).filter(CityGuideCategories.id == id).scalar()
    OBJ.title = title
    OBJ.fk = title
    session.commit()

def photos(id: int, photos: list):
    OBJ = session.query(CityGuideCategories).filter(CityGuideCategories.id == id).scalar()
    OBJ.photos = photos
    session.commit()
