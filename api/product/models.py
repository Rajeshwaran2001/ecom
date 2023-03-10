from django.db import models
from api.category.models import Category
# Create your models here.


class Product(models.Model):    
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1550)
    sku = models.CharField(max_length=50, null=True, blank=True)
    price = models.CharField(max_length=50)
    discountPercentage = models.CharField(max_length=2, null=True, blank=True)
    stock = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True, blank=True)
    farmerId = models.CharField(max_length=5, default=5, null=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True)
    isNew = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
