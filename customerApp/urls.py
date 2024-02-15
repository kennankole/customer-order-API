from django.urls import path
from customerApp import views

urlpatterns = [
  path('orders/', views.order_list),
]