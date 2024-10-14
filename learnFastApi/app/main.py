from fastapi import FastAPI
from enum import Enum

from app.database import engine
from app.models import todo_model
from app.routers import todo_router, support_router
from app.custom_exceptions import MyCustomException, custom_exception_handler

from starlette.middleware.base import BaseHTTPMiddleware
from app.middleware import add_process_time_header
from fastapi.middleware.cors import CORSMiddleware

class Tags(Enum):
    home :str = "Home"
    todo :str  = "Todo"
    support :str  = "Support"

tags_info=[{
    "name": Tags.home,
    "description": "Operations related to the home page"
}]

app = FastAPI(
    title="API by Python Swagger",
    description="This is a simple API created using FastAPI and Swagger",
    version="0.1.0",
    openapi_tags=tags_info
)
#app.title = "API by Python Swagger"


origins  = [
    "http://localhost:8080",
]

todo_model.Base.metadata.create_all(bind=engine)

app.include_router(todo_router.router)
app.include_router(support_router.router)

app.add_exception_handler(MyCustomException, custom_exception_handler)
app.add_middleware(BaseHTTPMiddleware, dispatch=add_process_time_header)
app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins, 
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"]
)

@app.get("/", tags=[Tags.home])
async def hello_world():
    return {"message": "Hola, Mundo!"}
