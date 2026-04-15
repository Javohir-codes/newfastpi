from fastapi import FastAPI, Request
from app.database import Base, engine
from app.routers import user, auth, products
from fastapi.templating import Jinja2Templates

Base.metadata.create_all(bind=engine)

app = FastAPI()
products_db = []

templates = Jinja2Templates(directory="app/templates")

app.include_router(user.router)
app.include_router(auth.router)

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
def home(request: Request):
    print(products.products_db)
    return templates.TemplateResponse("home.html", {
        "request": request,
        "products": products.products_db
    })

app.include_router(products.router)