from dotenv import load_dotenv
import os

from jinja_config import templates

from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

from db.create_db import create_tables
from weather import weather
from db.sessions.user_session import *
from db.sessions.admin_sessions.get_func import *
from admin import admin


# Router Setup
app = FastAPI()
app.include_router(admin, prefix='/admin')

# Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'], 
    allow_headers=['*'],
)
app.mount("/static", StaticFiles(directory="static"), name="static")
create_tables()
load_dotenv()
HOST = os.getenv('SERVER_HOST')
PORT = int(os.getenv('SERVER_PORT'))


# Frontend Views
class ProductPage:

    def __init__(self, header, description, photos, qr_code=None, footer=None) -> None:

        self.photos = photos
        self.header = header
        self.span = None
        self.body = description
        self.qr_code = qr_code

        desc_split = description.split('<span>')
        if len(desc_split) > 1:
            self.span = desc_split[0]
            self.body = desc_split[1]

        self.footer = { 'address':footer, 'phone':None } if footer else { }

        footer_split = footer.split('<phone>') if footer else []
        if len(footer_split) > 1:
            self.footer = { 'address':footer_split[0], 'phone':footer_split[1] }

    def to_dict(self): return {**self.__dict__}


class TemplateContext:

    # Privet Functions
    def __tile(self, row: tuple): return {
        'home' : lambda: { 'href':f"view?what=news&id={row[0]}", 'text':row[1], 'photos':row[3] },
        'info' : lambda: { 'href':f"view?what=info&id={row[0]}", 'text':row[1], 'photos':row[3] },
        'services' : lambda: { 'href':f"view?what=service&id={row[0]}", 'text':row[1], 'price':row[3], 'photos':row[4] },
        'recommended' : lambda: { 'href':f"view?what={row[0]}&id={row[1]}", 'text':row[2], 'photos':row[3] },
        'guide' : lambda: { 'href':f"guide-grouped?category={row[1]}", 'text':row[2], 'photos':row[3] },
        'menu' : lambda: { 'href':f"view?what=menu&id={row[0]}", 'text':row[1], 'price':row[3], 'photos':row[5] },
        'guide-grouped' : lambda: { 'href':f"view?what=guide&id={row[0]}", 'text':row[1], 'photos':row[5] }
    }.get(self.current_page)()

    __func = {
        'news' : get_news_by_id,
        'info' : get_about_by_id,
        'service' : get_service_by_id,
        'guide' : get_guide_by_id,
        'menu' : get_restaurant_by_id
    }

    def __get_content(self, target: str, id: int): 
        data = self.__func.get(target)(id); return {
            'news' : lambda: ProductPage(header=data[0], description=data[1], photos=data[2], qr_code=data[3]),
            'info' : lambda: ProductPage(header=data[0], description=data[1], photos=data[2]),
            'service' : lambda: ProductPage(header=data[0], description=data[1], photos=data[3]),
            'guide' : lambda: ProductPage(header=data[0], description=data[1], footer=data[2], photos=data[3], qr_code=data[4]),
            'menu' : lambda: ProductPage(header=data[0], description=data[1], photos=data[3], qr_code=data[4])
        }.get(target)().to_dict()


    # Global Context
    user_context: dict
    nav_bar_content: list = [
        { 'id' : 'home', 'text' : 'Главная' },
        { 'id' : 'info', 'text' : 'Об Отеле' },
        { 'id' : 'services', 'text' : 'Услуги Отеля' },
        { 'id' : 'recommended', 'text' : 'Рекомендуем' },
        { 'id' : 'guide', 'text' : 'Гид по Мариуполю' },
        { 'id' : 'menu', 'text' : 'Меню' },
        { 
            'id' : 'internet', 
            'text' : 'Телеканалы', 
            'href' : 'iptv://' 
        },
    ]
    
    @classmethod
    def fill_client_data(cls, device_id: int): cls.user_context = {
        'room' : get_device_by_id(device_id)[0],
        'temp' : weather()[0],
        'cond' : weather()[1]
    }


    # Narrow Context
    def __init__(self, request: Request,
                 
        current_page: str = None, 
        solid_background = False,
        title: str = None,
        guide_category: str = None,
        content_query: dict = None,

    ) -> None:
        
        self.request = request
        self.current_page = current_page
        self.solid_background = solid_background
        self.title = title
        self.guide_category = guide_category
        self.content = self.__get_content(content_query['what'], content_query['id']) if content_query else None

    @property
    def tile_content(self): return {
        'home' : lambda: [dict(self.__tile(row)) for row in get_all_news()],
        'info' : lambda: [dict(self.__tile(row)) for row in get_all_about()],
        'services' : lambda: [dict(self.__tile(row)) for row in get_all_services()],
        'recommended' : lambda: [dict(self.__tile(row)) for row in get_all_recommendations()],
        'guide' : lambda: [dict(self.__tile(row)) for row in get_all_categories()],
        'menu' : lambda: [dict(self.__tile(row)) for row in get_restaurant_menu()],
        'guide-grouped' : lambda: [dict(self.__tile(row)) for row in get_all_guides(self.guide_category)],
        'product-page' : lambda: None,
    }.get(self.current_page)()


    # Output Dictionary
    def to_dict(self): return { 
        'user_context': TemplateContext.user_context,
        'nav_bar_content': TemplateContext.nav_bar_content,
        'tile_content' : self.tile_content,
        **self.__dict__ 
    }
  
@app.get('/{device_id}')
def _(device_id: int):
    TemplateContext.fill_client_data(device_id)
    return RedirectResponse(url=f'{device_id}/home')


@app.get('/{device_id}/home', response_class=HTMLResponse)
def _(request: Request, device_id: int): 
    TemplateContext.fill_client_data(device_id)
    return templates.TemplateResponse('home.html', TemplateContext(
        request=request,
        solid_background = True,
        current_page='home',
        content_query={ 'what':'news', 'id':get_all_news()[0][0] }
    ).to_dict())
    

@app.get('/{device_id}/info', response_class=HTMLResponse)
def _(request: Request, device_id: int): 
    TemplateContext.fill_client_data(device_id)
    return templates.TemplateResponse('info.html', TemplateContext(
        request=request,
        current_page='info',
    ).to_dict())


@app.get('/{device_id}/services', response_class=HTMLResponse)
def _(request: Request, device_id: int): 
    TemplateContext.fill_client_data(device_id)
    return templates.TemplateResponse('tiles.html', TemplateContext(
        request=request,
        current_page='services',
        title='Услуги Отеля'
    ).to_dict())


@app.get('/{device_id}/recommended', response_class=HTMLResponse)
def _(request: Request, device_id: int): 
    TemplateContext.fill_client_data(device_id)
    return templates.TemplateResponse('tiles.html', TemplateContext(
        request=request,
        current_page='recommended',
        title='Рекомендуем'
    ).to_dict())


@app.get('/{device_id}/guide', response_class=HTMLResponse)
def _(request: Request, device_id: int): 
    TemplateContext.fill_client_data(device_id)
    return templates.TemplateResponse('tiles.html', TemplateContext(
        request=request,
        current_page='guide',
        title='Гид по Мариуполю'
    ).to_dict())
    

@app.get('/{device_id}/menu', response_class=HTMLResponse)
def _(request: Request, device_id: int): 
    TemplateContext.fill_client_data(device_id)
    return templates.TemplateResponse('tiles.html', TemplateContext(
        request=request,
        current_page='menu',
        title='Меню отеля'
    ).to_dict())


@app.get('/{device_id}/guide-grouped', response_class=HTMLResponse)
def _(request: Request, device_id: int): 
    TemplateContext.fill_client_data(device_id)
    return templates.TemplateResponse('tiles.html', TemplateContext(
        request=request,
        current_page='guide-grouped',
        title=request.query_params.get('category'),
        guide_category=request.query_params.get('category')
    ).to_dict())


@app.get('/{device_id}/view', response_class=HTMLResponse)
def _(request: Request, device_id: int): 
    TemplateContext.fill_client_data(device_id)
    return templates.TemplateResponse('product-page.html', TemplateContext(
        request=request,
        solid_background=True,
        current_page='product-page',
        content_query=request.query_params
    ).to_dict())


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=HOST, port=PORT)