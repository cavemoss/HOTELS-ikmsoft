from fastapi import APIRouter, Request
import db.sessions.admin_sessions.updates_func.applications as edit_applications

edit = APIRouter()

@edit.post("/name")
def _(id: int, value: str):
    edit_applications.name(id, value)

@edit.post("/resource-url")
def _(id: int, value: str):
    edit_applications.resource_url(id, value)

@edit.post("/photos")
async def _(request: Request, id: int):
    body = await request.json()
    edit_applications.photos(id, body['photos'])
