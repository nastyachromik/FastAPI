from pydantic import BaseModel
from fastapi import APIRouter

prod_router = APIRouter(prefix='/products', tags=['products'])

class Product(BaseModel):
    id: int
    name: str
    price: int | float

@prod_router.get('/all_products', status_code=200)
async def all_products():
    pass

@prod_router.get('/get_product', status_code=200)
async def get_product(id: int):
    pass

@prod_router.post('/create', status_code=201)
async def create_product(product: Product):
    pass

@prod_router.delete('/delete', status_code=200)
async def delete_product(product_id: int):
    pass

@prod_router.put('/put', status_code=201)
async def put_product(product: Product):
    pass
