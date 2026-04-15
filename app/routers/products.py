from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()
products_db = []

class Product(BaseModel):
    name: str
    price: float
    image: str

@router.post("/products")
def create_product(product: Product):
    products_db.append(product)
    return {"message": "Товар добавлен"}

@router.get("/products")
def get_products():
    return products_db