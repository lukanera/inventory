from . import views
from django.urls import path
from rest_framework.routers import SimpleRouter

from .models import Category
from .views import ProductViewSet, CategoryViewSet, CategoryItemsViewSet

router = SimpleRouter()
router.register('items', ProductViewSet)
router.register('categories', CategoryViewSet)
router.register('caregories/<int:category_id>/items/', CategoryItemsViewSet, basename='category-itmes')

urlpatterns = router.urls
