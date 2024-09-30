from fastapi import APIRouter, Request
import db.sessions.admin_sessions.updates_func.main_news as edit_news

edit = APIRouter()

@edit.post("/title")
def _(id: int, value: str):
    edit_news.title(id, value)

@edit.post("/description")
def _(id: int, value: str):
    edit_news.description(id, value)

@edit.post("/photos")
async def _(request: Request, id: int):
    body = await request.json()
    edit_news.photos(id, body['photos'])

@edit.post("/qr-url")
def _(id: int, value: str):
    edit_news.qr_url(id, value)
