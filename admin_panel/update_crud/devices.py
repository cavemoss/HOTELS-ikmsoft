from fastapi import APIRouter
import db.sessions.admin_sessions.updates_func.devices as edit_devices

edit = APIRouter()

@edit.post("/room-number")
def _(id: int, value: int):
    edit_devices.room_number(id, value)

@edit.post("/device-status")
def _(id: int, value: str):
    edit_devices.device_status(id, value)
