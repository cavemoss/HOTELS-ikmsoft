from fastapi import APIRouter, Request
import db.sessions.admin_sessions.updates_func.city_guide_categories as edit_guide_categories

edit = APIRouter()

@edit.post("/title")
def _(id: int, value: str):
    edit_guide_categories.title(id, value)

@edit.post("/photos")
async def _(request: Request, id: int):
    body = await request.json()
    edit_guide_categories.photos(id, body['photos'])