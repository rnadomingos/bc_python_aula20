from sqlalchemy.orm import Session
from schemas import ProductCreate, ProductUpdate
from models import ProductModel


def get_products(db: Session):
    '''
    Get all products from models
    '''
    return db.query(ProductModel).all()


def get_product(product_id: int, db: Session):
    '''
    Get a product by id from models
    '''
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()

def create_product(db: Session, product:ProductCreate):
    '''
    Add a product in products table
    '''
    db_product = ProductModel(**product.model_dump()) 
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    '''
    Delete a product by id from products table
    '''
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if db_product is None:
        return None
    
    db.delete(db_product)
    db.commit()
    return db_product
    
def update_product(db: Session, product_id: int, product: ProductUpdate):
    '''
    Update a product by id from products table
    '''
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

    if db_product is None:
        return None
    
    if product.name is not None:
        db_product.name = product.name
    
    if product.description is not None:
        db_product.description = product.description
    
    if product.price is not None:
        db_product.price = product.price
    
    if product.category is not None:
        db_product.category = product.category

    if product.supplier_email is not None:
        db_product.supplier_email = product.supplier_email  

    db.commit()
    db.refresh(db_product)  
    return db_product    