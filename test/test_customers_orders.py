import pytest
import json
from rest_framework.test import APIRequestFactory
from customerApp import views
from django.urls import reverse
from rest_framework import status
from customerApp.serializers import CustomerSerializer, OrderSerializer
from customerApp.models import Customer, Order


@pytest.fixture
def api_factory():
  return APIRequestFactory()

@pytest.fixture
def view():
  return views.customer_detail

@pytest.mark.django_db
def test_create_customer(api_factory):
  factory = api_factory
  data = {'username': 'bob', 'code': 'X7YZ9'}
  request = factory.post('/customers/', json.dumps(data), content_type='application/json')
  
  view = views.customers_list
  response = view(request)
  assert response.status_code == status.HTTP_201_CREATED

  assert Customer.objects.count() == 1
  customer = Customer.objects.get(pk=1)
  assert customer.username == 'bob'
  assert customer.code == 'X7YZ9'

@pytest.mark.django_db
def test_fetch_all_customers(api_factory):
  factory = api_factory
  request = factory.get('/customers/')
  view = views.customers_list
  response = view(request)
  assert response.status_code == 200
  customers = Customer.objects.all()
  serializer = CustomerSerializer(customers, many=True)
  
  assert response.data == serializer.data


@pytest.mark.django_db
def test_customer_detail(api_factory, view):
  customer = Customer.objects.create(username="tony", code="SBS56")
  customer.save()

  factory = api_factory
  url = reverse('customers', args=[customer.pk])
  
  request = factory.get(url)
  response = view(request, pk=customer.pk)
  
  assert response.status_code == status.HTTP_200_OK
  serializer = CustomerSerializer(customer)
  assert response.data == serializer.data
  
  
@pytest.mark.django_db
def test_customer_profile_post_order(api_factory, view):
  customer = Customer.objects.create(username="Joel", code="FGT56")
  customer.save()
  
  factory = api_factory
  url = reverse("customers", args=[customer.pk])
  
  order_data = {
    'item': 'laptop',
    'amount': 200,
    'customer': customer.pk
  }

  request = factory.post(url, data=json.dumps(order_data), content_type='application/json')
  response = view(request, pk=customer.pk)
  
  assert response.status_code == status.HTTP_201_CREATED
  
  order = Order.objects.get(customer=customer)
  serialized_data = OrderSerializer(order)
  assert response.data == serialized_data.data

@pytest.mark.django_db
def test_fetch_all_orders():
  factroy = APIRequestFactory()
  
  request = factroy.get('/orders/')
  view = views.order_list
  response = view(request)
  
  assert response.status_code == 200
  
  orders = Order.objects.all()
  serializer = OrderSerializer(orders, many=True)
  
  assert response.data == serializer.data