import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Product_Inventory.settings")

django.setup()

from fastapi import FastAPI
from myapp.controller import product_router


app = FastAPI()

app.include_router(product_router,prefix="/product",tags=["Product"])



