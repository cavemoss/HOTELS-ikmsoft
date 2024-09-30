from fastapi import APIRouter, Request
import db.sessions.admin_sessions.updates_func.about as edit_about

edit = APIRouter()

@edit.post("/title")
def _(id: int, value: str):
    edit_about.title(id, value)

@edit.post("/description")
def _(id: int, value: str):
    edit_about.description(id, value)

@edit.post("/photos")
async def _(request: Request, id: int):
    body = await request.json()
    edit_about.photos(id, body['photos'])
