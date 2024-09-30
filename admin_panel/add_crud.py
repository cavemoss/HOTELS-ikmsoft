from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from db.sessions.admin_sessions.add_func import *

add = APIRouter()

def include_CORS(message = { }):
    response = JSONResponse(message)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    return response

@add.post('/device') 
def _(room_number: int, device_status: str):
    add_device(room_number, device_status)
    return include_CORS()

@add.post('/news') 
async def _(request: Request, title: str, description: str, qr_url: str):
    body = await request.json()
    add_news(title, description, body['photos'], qr_url)
    return include_CORS()

@add.post('/about') 
async def _(request: Request, title: str, description: str):
    body = await request.json()
    add_about(title, description, body['photos'])
    return include_CORS()

@add.post('/service')
async def _(request: Request, name: str, description: str, price: int):
    body = await request.json()
    add_service(name, description, price, body['photos'])
    return include_CORS()

@add.post('/guide-category')
async def _(request: Request, title: str):
    if check_category(title):
        body = await request.json()
        add_guide_category(title, body['photos'])
        return include_CORS()
    else: return include_CORS({"error": "Category already exists!"})

@add.post('/city-guide')
async def _(request: Request, placename: str, description: str, address: str, category: str, recommended: int, qr_url: str):
    body = await request.json()
    add_guide(placename, description, address, category, bool(recommended), body['photos'], qr_url)
    return include_CORS()

@add.post('/menu') 
async def _(request: Request, name: str, description: str, price: int, recommended: int, qr_url: str):
    body = await request.json()
    add_menu(name, description, price, bool(recommended), body['photos'], qr_url)
    return include_CORS()

@add.post('/app') 
async def _(request: Request, name: str, resource_url: str):
    body = await request.json()
    add_app(name, resource_url, body['photos'])
    return include_CORS()
