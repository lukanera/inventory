from django.db import models
from core.models import BaseModel
from random import choice
from string import digits


class Item(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField
    height = models.FloatField(null=True, blank=True)
    width = models.FloatField(null=True, blank=True)
    length = models.FloatField(null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='items')
    stock_qty = models.PositiveIntegerField
    expiration_date = models.DateTimeField(null=True)
    barcode = models.CharField(max_length=13, unique=True, editable=False, blank=True)

    def save(self, *args, **kwargs):
        self.barcode = ''.join(choice(digits) for i in range(13))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Category(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name