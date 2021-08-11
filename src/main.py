from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
async def healthcheck():
    '''
    check the server in work    
    '''

    return {'ping' : 'pong'}
