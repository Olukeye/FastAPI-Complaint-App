from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from routes import users

app = FastAPI()


app.include_router(users.router)
# app.include_router(category.router)
# app.include_router(stock.router)


# Middleware to catch actual internal response errors  
async def catch_exception_middleware(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=jsonable_encoder({"details": str(e)}))

app.middleware('http')(catch_exception_middleware)


@app.get('/')
async def root():
    return {"Hello Complainers!"}
    
    
if __name__ == '__main__':
    uvicorn.run(app, port=7000, host='0.0.0.0')