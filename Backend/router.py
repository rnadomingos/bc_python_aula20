from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schemas import ProductResponse, ProductCreate, ProductUpdate
from typing import List
from crud import (
    create_product, 
    get_product,
    get_products, 
    delete_product, 
    update_product 
)

router = APIRouter()

@router.get("/products/", response_model=List[ProductResponse])
def read_all_products(db: Session = Depends(get_db)):
     '''
     List all products.
     '''
     db_products = get_products(db)
     return db_products

@router.get("/products/{product_id}", response_model=ProductResponse)
def read_product_by_id(product_id: int, db: Session = Depends(get_db)):
     '''
     List a product by ID.
     '''
     db_product = get_product(product_id, db)
     if db_product is None:
          raise HTTPException(status_code=404, detail="Product id not found. Check ID")
     return db_product

@router.post("/products/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
     '''
     Add a products.
     '''
     return create_product(product, db)

@router.delete("/products/", response_model=ProductResponse)
def delete_product_by_id(product_id: int, db: Session = Depends(get_db)):
     '''
     Delete a product by ID.
     '''
     db_product = delete_product(product_id, db)
     if db_product is None:
          raise HTTPException(status_code=404, detail="Product id not found. Check ID")
     return db_product

@router.put("products/{product_id}", response_model=ProductResponse)
def update_product_by_id(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
     '''
     Update a product by ID.
     '''
     db_product = update_product(product_id, product, db)
     if db_product is None:
          raise HTTPException(status_code=404, detail="Product id not found. Check ID")
     return db_product