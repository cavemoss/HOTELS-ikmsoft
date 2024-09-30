from fastapi import APIRouter
from fastapi.responses import JSONResponse

from db.sessions.admin_sessions.delete_func import *

delete_api = APIRouter()

def include_CORS():
    response = JSONResponse({ })
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    return response 

@delete_api.delete("/device")
def _(id: int):
    delete_device(id)
    return include_CORS()

@delete_api.delete("/news")
def _(id: int):
    delete_news(id)
    return include_CORS()

@delete_api.delete('/about')
def _(id: int):
    delete_about(id)
    return include_CORS()

@delete_api.delete("/service")
def _(id: int):
    delete_service(id)
    return include_CORS()

@delete_api.delete('/guide-category')
def _(id: int):
    delete_category(id)
    return include_CORS()

@delete_api.delete("/city-guide")
def _(id: int):
    delete_guide(id)
    return include_CORS()

@delete_api.delete("/menu")
def _(id: int):
    delete_menu(id)
    return include_CORS()

@delete_api.delete("/app")
def _(id: int):
    delete_app(id)
    return include_CORS()
