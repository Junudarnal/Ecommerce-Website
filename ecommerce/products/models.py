from django.db import models
from products.constant import PRODUCTCATEGORY, STOCK, STATUS
import uuid


class Products(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=60, default='')
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=500, default='', blank=True, null=True)
    color = models.CharField(max_length=250, default='', blank=True, null=True)
    stock = models.CharField(max_length = 200,choices= STOCK, default="")
    status = models.CharField(max_length = 200,choices= STATUS, default="")
    image = models.ImageField(upload_to='static/img/')
    category = models.CharField(choices=PRODUCTCATEGORY, default="All", max_length=100)
    quantity = models.IntegerField(null = False, blank = False , default = "1")

    def __str__(self) -> str:
        return self.name

