from pydantic import BaseModel, PositiveFloat, PositiveInt, EmailStr, validate_email
from datetime import datetime
from typing import Optional

class ProductBase(BaseModel):
    name: str
    description: str
    price: PositiveFloat
    category: str
    supplier_email: EmailStr

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: PositiveInt
    created_at: datetime

    class Config:
        from_attributes = True

class ProductUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    price: Optional[PositiveFloat]
    category: Optional[str]
    supplier_email: Optional[EmailStr]