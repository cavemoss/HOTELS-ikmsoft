from fastapi import APIRouter, Request
import db.sessions.admin_sessions.updates_func.hotel_services as edit_services

edit = APIRouter()

@edit.post("/name")
def _(id: int, value: str):
    edit_services.name(id, value)

@edit.post("/description")
def _(id: int, value: str):
    edit_services.description(id, value)

@edit.post("/price")
def _(id: int, value: int):
    edit_services.price(id, value)

@edit.post("/photos")
async def _(request: Request, id: int):
    body = await request.json()
    edit_services.photos(id, body['photos'])
