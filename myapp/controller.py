from typing import List

from fastapi import APIRouter, HTTPException

from myapp.models import Product
from myapp.schema import ProductOut, ProductIn

product_router = APIRouter()


# EndPoint for getting all product
@product_router.get("/all-products", response_model=List[ProductOut])
def get_all_products():
    products = Product.objects.all()
    return products


# EndPoint for getting product by product_id
@product_router.get('/{product_id}', response_model=ProductOut)
def get_product_by_id(product_id: int):
    product = Product.objects.filter(id=product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product Not Found or Wrong Id")
    return product


# EndPoint for update product by product_id
@product_router.put("/{product_id}")
def update_product_by_id(product_id: int, product_in: ProductIn):
    product = Product.objects.filter(id=product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product Not Found or Wrong Id")
    Product.objects.filter(id=product_id).update(**product_in.dict())
    return {"message": "Product updated successfully"}




# EndPoint for delete product by product_id
@product_router.delete("/{product_id}")
def delete_product_by_id(product_id: int):
    product = Product.objects.filter(id=product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product Not Found or Wrong Id")
    Product.objects.filter(id=product_id).delete()
    return {"message": "Product deleted successfully"}
