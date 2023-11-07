from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_router


app = FastAPI()
app.title = "Mi aplicación con  FastAPI"
app.version = "0.0.1"
app.add_middleware(ErrorHandler)

app.include_router(movie_router)
app.include_router(user_router)

Base.metadata.create_all(bind=engine)


class User(BaseModel):
    email: str
    password: str


@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')
