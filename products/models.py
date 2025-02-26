from django.db import models
from core.models import BaseModel

class Item(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField
    height = models.FloatField(null=True, blank=True)
    width = models.FloatField(null=True, blank=True)
    length = models.FloatField(null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='items')
    stock_qty = models.PositiveIntegerField
    expiration_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.name

class Category(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name