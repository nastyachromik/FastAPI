from fastapi import APIRouter
from pydantic import BaseModel

category_router = APIRouter(prefix='/category', tags=['category'])

class Category(BaseModel):
    id: int
    name: str
    attr: dict

@category_router.get('/all_categories', status_code=200)
async def all_categories():
    pass

@category_router.get('/get_category', status_code=200)
async def get_category(id: int):
    pass

@category_router.post('/create', status_code=201)
async def create_category(category: Category):
    pass

@category_router.put('/put', status_code=201)
async def put_category(category: Category):
    pass

@category_router.delete('/delete', status_code=200)
async def delete_category(id: Category.id):
    pass