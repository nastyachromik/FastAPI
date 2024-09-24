from fastapi import FastAPI
from routers.category import category_router
from routers.products import prod_router
import uvicorn

app = FastAPI()
app.include_router(category_router)
app.include_router(prod_router)

if __name__ == '__main__':
    uvicorn.run(app)
