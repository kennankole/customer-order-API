from django.urls import path, include
from rest_framework.routers import DefaultRouter
from customerApp import views

router = DefaultRouter()

router.register(r'customers', views.CustomerViewSet, basename="customers"),
router.register(r'orders', views.OrderViewSet, basename="orders"),
# router.register(r'api-customer-login', views.CustomerLogIn.as_view()),
urlpatterns = [
  # 
  path('', include(router.urls)),
  path('api-customer-login/', views.CustomerLogIn.as_view(), name="customer_login")
]

# urlpatterns = format_suffix_patterns(urlpatterns)