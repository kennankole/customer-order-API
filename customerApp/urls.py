from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from customerApp import views

urlpatterns = [
  path('orders/', views.OrderList.as_view(), name="orders"),
  path('orders/<int:pk>/', views.OrderDetail.as_view(), name="orders"),
  path('customers/', views.CustomerList.as_view(), name="customers"),
  path('customers/<int:pk>/', views.CustomerDetail.as_view(), name="customers")
]

urlpatterns = format_suffix_patterns(urlpatterns)