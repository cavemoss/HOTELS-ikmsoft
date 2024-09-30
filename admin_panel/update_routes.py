from fastapi import APIRouter
from admin_panel.update_crud.devices import edit as edit_devices
from admin_panel.update_crud.main_news import edit as edit_main_news
from admin_panel.update_crud.about import edit as edit_about
from admin_panel.update_crud.hotel_services import edit as edit_services
from admin_panel.update_crud.city_guide_categories import edit as edit_guide_categories
from admin_panel.update_crud.city_guides import edit as edit_guides
from admin_panel.update_crud.restaurant import edit as edit_restaurant
from admin_panel.update_crud.application import edit as edit_applications

edit = APIRouter()

edit.include_router(edit_devices, prefix="/device")
edit.include_router(edit_main_news, prefix="/news")
edit.include_router(edit_about, prefix="/about")
edit.include_router(edit_services, prefix="/service")
edit.include_router(edit_guide_categories, prefix="/guide-category")
edit.include_router(edit_guides, prefix="/guide")
edit.include_router(edit_restaurant, prefix="/restaurant")
edit.include_router(edit_applications, prefix="/app")
