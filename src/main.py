from fastapi import FastAPI

from src.api.service import product_router

app = FastAPI()

app.include_router(
    product_router,
    prefix="/product",
    tags=["Product"],
)

@app.get("/ping")
async def healthcheck():
    '''
    check the server in work    
    '''

    return {'ping' : 'pong'}


