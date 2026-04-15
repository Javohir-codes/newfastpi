from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from app.database import SessionLocal, get_db
from app import models
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/clothes", tags=["Clothes"])

templates = Jinja2Templates(directory="app/templates")


@router.post("/")
def create_clothes(name: str, price: int, image_url: str, db: Session = Depends(get_db)):
    item = models.Clothes(
        name=name,
        price=price,
        image_url=image_url
    )
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@router.get("/", response_class=HTMLResponse)
def read_products(request: Request, db: Session = Depends(get_db)):
    products = db.query(models.Clothes).all()
    print("PRODUCTS:", products)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "products": products
    })