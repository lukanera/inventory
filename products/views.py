from django.shortcuts import render
from .models import Item, Category
from rest_framework import viewsets
from .serializers import ItemSerializer, CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer