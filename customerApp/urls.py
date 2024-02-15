from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from customerApp import views

urlpatterns = [
  path('customers/', views.customers_list, name='customers'),
]

urlpatterns = format_suffix_patterns(urlpatterns)