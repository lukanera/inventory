from django.shortcuts import render
from unicodedata import category

from .models import Item, Category
from rest_framework import viewsets
from .serializers import ItemSerializer, CategorySerializer, CategoryItemSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryItemsViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = CategoryItemSerializer


    def get_queryset(self):
        return self.queryset.filter(category_id=self.kwargs['category_id'])

    def perform_create(self, serializer):
        serializer.save(category_id=self.kwargs['category_id'])