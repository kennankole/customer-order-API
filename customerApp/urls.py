from django.urls import path, include
from rest_framework.routers import DefaultRouter
from customerApp import views

router = DefaultRouter()

router.register(r'customers', views.CustomerViewSet, basename="customers"),
router.register(r'orders', views.OrderViewSet, basename="orders"),

urlpatterns = [
  path('', include(router.urls)),
]

