from pydantic import BaseModel


class  ProductIn(BaseModel):
    name:str
    category:str
    price:float


class ProductOut(BaseModel):
    name: str
    category: str
    price: float




