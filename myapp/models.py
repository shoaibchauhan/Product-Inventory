from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500, blank=False, null=False)
    category = models.CharField(max_length=250, blank=False, null=False)
    price = models.FloatField(blank=False, null=False)

    class Meta:
        db_table = 'Product_table'
        verbose_name = 'Product'