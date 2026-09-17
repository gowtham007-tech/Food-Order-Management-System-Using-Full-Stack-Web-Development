from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FoodOrderViewSet

router = DefaultRouter()
router.register('orders', FoodOrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
