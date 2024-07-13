from fastapi import APIRouter, HTTPException, Depends
from app.models import Category
from app.database import SessionLocal

router = APIRouter()


@router.get("/")
async def read_categories():
    db = SessionLocal()
    categories = db.query(Category).all()
    db.close()
    return categories


@router.get("/{category_id}")
async def read_category(category_id: int):
    db = SessionLocal()
    category = db.query(Category).filter(Category.category_id == category_id).first()
    db.close()
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.post("/")
async def create_category(name: str, description: str):
    db = SessionLocal()
    category = Category(name=name, description=description)
    db.add(category)
    db.commit()
    db.close()
    return {"msg": "Category created successfully"}

@router.put("/{category_id}")
async def update_category(category_id: int, name: str, description: str):
    db = SessionLocal()
    category = db.query(Category).filter(Category.category_id == category_id).first()
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    category.name = name
    category.description = description
    db.commit()
    db.close()
    return {"msg": "Category updated successfully"}

# get N of product 
@router.get("/products")
async def category_products(category_id: int):
    db = SessionLocal()
    category = db.query(Category).filter(Category.category_id == category_id).first()
    category_products = category.products
    db.close()
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category_products
