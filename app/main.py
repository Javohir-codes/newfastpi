from fastapi import FastAPI, Request, Depends
from sqlalchemy.orm import Session
from app.database import Base, engine, get_db
from app.routers import user, auth, products
from fastapi.templating import Jinja2Templates
from app import models


Base.metadata.create_all(bind=engine)

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(products.router)

@app.get("/")
def root(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )

@app.get("/register-page")
def register_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="register.html",
        context={"request": request}
    )

@app.get("/login-page")
def register_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={"request": request}
    )

@app.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    items = db.query(models.Clothes).all()

    return templates.TemplateResponse("index.html", {
        "request": request,
        "products": items
    })