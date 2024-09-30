from fastapi import APIRouter, Request
import db.sessions.admin_sessions.updates_func.restaurant as edit_restaurant

edit = APIRouter()

@edit.post("/name")
def _(id: int, value: str):
    edit_restaurant.name(id, value)

@edit.post("/description")
def _(id: int, value: str):
    edit_restaurant.description(id, value)

@edit.post("/price")
def _(id: int, value: int):
    edit_restaurant.price(id, value)

@edit.post("/recommended")
def _(id: int, value: int):
    edit_restaurant.recommended(id, bool(value))

@edit.post("/photos")
async def _(request: Request, id: int):
    body = await request.json()
    edit_restaurant.photos(id, body['photos'])

@edit.post("/qr-url")
def _(id: int, value: str):
    edit_restaurant.qr_url(id, value)
