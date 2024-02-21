import pytest
import json
from rest_framework.test import APIRequestFactory, APIClient
from django.contrib.auth import get_user_model

from rest_framework import status
from customerApp.serializers import CustomerSerializer, OrderSerializer
from customerApp.models import Customer, Order
from customerApp import views

Customer = get_user_model()

@pytest.fixture
def api_client():
  customer = Customer.objects.create_user(username="testcustomer", password="qwerty", customer_code="SDR90")
  customer.save()
  client = APIClient()
  client.login(username="testcustomer", password="qwerty")
  return client

@pytest.fixture
def api_factory():
  return APIRequestFactory()


@pytest.mark.django_db
def test_customer_login(api_client):
  client = api_client
  data = {
    'username': 'testcustomer',
    'password': 'qwerty'
  }
  response = client.post('/api-customer-login/', data=data, format='json')

  assert response.status_code == status.HTTP_200_OK
  assert 'token' in response.data
  
@pytest.mark.django_db
def test_create_customer(api_client):
  factory = api_client
  
  data = {'username': 'bob', 'customer_code': 'X7YZ9', 'password': 'qwerty', 'orders': []}
  response = factory.post('/customers/', json.dumps(data), content_type='application/json')

  assert response.status_code == status.HTTP_201_CREATED

  assert response.data['username'] == 'bob'
  assert response.data['customer_code'] == 'X7YZ9'

@pytest.mark.django_db
def test_customer_list_and_detail(api_client):
  factory = api_client
  
  response = factory.get('/customers/')
  
  assert response.status_code == status.HTTP_200_OK

  customers = Customer.objects.all()
  serializer = CustomerSerializer(customers, many=True)
  
  assert response.data == serializer.data

  customer = Customer.objects.get(username=response.data[0]['username'])
  
  request = factory.get(f"/customers/{customer.pk}/")
  assert request.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_create_order(api_client):
  factory = api_client
  response = factory.get('/customers/')
  
  customer = Customer.objects.get(username=response.data[0]['username'])
  data = {
    'item': 'laptop', 
    'amount': '1000', 
    'customer': customer.pk
  }
  request = factory.post("/orders/", data, format='json')
  
  assert request.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_order_list_and_detail(api_client):
  factory = api_client
  response = factory.get("/orders/")
  
  assert response.status_code == status.HTTP_200_OK

  orders = Order.objects.all()
  serializer = OrderSerializer(orders, many=True)
  
  assert response.data == serializer.data
