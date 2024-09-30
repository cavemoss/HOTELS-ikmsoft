from db.create_db import create_session
from db.models import DeviceStatus, Devices

session = create_session()

device_status_enum = {
    'ONLINE' : DeviceStatus.ONLINE,
    'OFFLINE' : DeviceStatus.OFFLINE,
    'STANDBY' : DeviceStatus.STANDBY,
    'MALFUNCTION' : DeviceStatus.MALFUNCTION
}

def room_number(id: int, room: int):
    OBJ = session.query(Devices).filter(Devices.id == id).scalar()
    OBJ.room_number = room
    session.commit()

def device_status(id: int, device_status_str: str):
    OBJ = session.query(Devices).filter(Devices.id == id).scalar()
    OBJ.device_status = device_status_enum[device_status_str]
    session.commit()
