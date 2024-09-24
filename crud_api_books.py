from fastapi import FastAPI, HTTPException, status, Path, Query
import uvicorn
from pydantic import BaseModel


api = FastAPI()

books = {}
class Message(BaseModel):
    id: int
    """= Path(min_length=4, max_length=8, description="Enter book id")"""
    name: str
    author: str
    year: int
    """= Path(min_length=1, max_length=4)"""
    price: float | int

@api.get('/')
async def get_all():
    return books

@api.get('/{book_id}', status_code=status.HTTP_200_OK)
async def get_book(book_id: int = Path(min_length=4, max_length=8, description="Enter book id")):
    try:
        return books[book_id]
    except KeyError:
        raise HTTPException(status_code=404, detail='record not found')

@api.post('/book', status_code=status.HTTP_201_CREATED)
async def add_book(message: Message):
    new_book = {}
    new_book['name'] = message.name
    new_book['author'] = message.author
    new_book['year'] = message.year
    new_book['price'] = message.price
    books[message.id] = new_book
    return {'status_code': 200,
            'message': 'Record has been created'}

@api.put('/book', status_code=status.HTTP_201_CREATED)
async def fix_book(message: Message):
    try:
        book_id = message.id
        books[book_id]['name'] = message.name
        books[book_id]['author'] = message.author
        books[book_id]['year'] = message.year
        books[book_id]['price'] = message.price
        return {'status_code': 200,
            'message': 'Record has been created'}
    except KeyError:
        raise HTTPException(status_code=404, detail='record not found')

@api.delete('/book')
async def delete_book(book_id: int):
    try:
        del books[book_id]
        return {'status_code': 200,
            'message': 'Record has been deleted'}
    except KeyError:
        raise HTTPException(status_code=404, detail='record not found')
    
if __name__ == '__main__':
    uvicorn.run(api)

