from db.create_db import create_session
from db.models import MainNews

session = create_session()

def title(id: int, title: str):
    OBJ = session.query(MainNews).filter(MainNews.id == id).scalar()
    OBJ.title = title
    session.commit()

def description(id: int, description: str):
    OBJ = session.query(MainNews).filter(MainNews.id == id).scalar()
    OBJ.description = description
    session.commit()

def photos(id: int, photos: list):
    OBJ = session.query(MainNews).filter(MainNews.id == id).scalar()
    OBJ.photos = photos
    session.commit()

def qr_url(id: str, qr_url: str) -> None:
    OBJ = session.query(MainNews).filter(MainNews.id == id).scalar()
    OBJ.qr_url = qr_url
    session.commit()