from . import views
from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import ProductViewSet, CategoryViewSet

router = SimpleRouter()
router.register(r'users', ProductViewSet)
router.register(r'accounts', CategoryViewSet)

urlpatterns = router.urls
