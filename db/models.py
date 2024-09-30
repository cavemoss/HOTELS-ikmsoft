import enum
import json
from sqlalchemy.orm import declarative_base
from sqlalchemy import TypeDecorator, VARCHAR, Integer, Column, Text, ForeignKey, Boolean
from sqlalchemy.types import Enum

Base = declarative_base()


class ListType(TypeDecorator):
    impl = VARCHAR

    def process_bind_param(self, value, dialect):
        if value is not None: value = json.dumps(value)
        return value

    def process_result_value(self, value, dialect):
        if value is not None: value = json.loads(value)
        return value


class DeviceStatus(enum.Enum):
    ONLINE = 'ONLINE'
    OFFLINE = 'OFFLINE'
    STANDBY = 'STANDBY'
    MALFUNCTION = 'MALFUNCTION'
    

class Devices(Base):
    __tablename__ = 'devices'

    id = Column(Integer, primary_key=True)
    room_number = Column(Integer)
    device_status = Column(Enum(DeviceStatus))


class MainNews(Base):
    __tablename__ = 'main_news'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    description = Column(Text)
    photos = Column(ListType)
    qr_url = Column(Text)


class About(Base):
    __tablename__ = 'about'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    description = Column(Text)
    photos = Column(ListType)

    
class HotelServices(Base):
    __tablename__ = 'hotel_services'

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    description = Column(Text)
    price = Column(Integer)
    photos = Column(ListType)


class CityGuideCategories(Base):
    __tablename__ = 'city_guide_categories'

    id = Column(Integer, primary_key=True)
    fk = Column(Text)
    
    title = Column(Text)
    photos = Column(ListType)


class CityGuides(Base):
    __tablename__ = 'city_guides'

    id = Column(Integer, primary_key=True)
    category = Column(Text, ForeignKey('city_guide_categories.fk'))

    placename = Column(Text)
    description = Column(Text)
    address = Column(Text)
    recommended = Column(Boolean)
    photos = Column(ListType)
    qr_url = Column(Text)


class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    description = Column(Text)
    price = Column(Integer)
    recommended = Column(Boolean)
    photos = Column(ListType)
    qr_url = Column(Text)


class Applications(Base):
    __tablename__ = 'applications'

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    resource_url = Column(Text)
    photos = Column(ListType)