import pytest
from rest_framework.test import APIRequestFactory, APIClient
from customerApp.views import customers_list, order_list
from customerApp.serializers import CustomerSerializer, OrderSerializer
from customerApp.models import Customer, Order

@pytest.fixture
def api_client():
  return APIClient()

@pytest.mark.django_db
def test_customers_list(api_client):
  Customer.objects.create(username='alice', code='W2BC5')
  Customer.objects.create(username='john', code='SB45W')

  factory = APIRequestFactory()

  request = factory.get('/customers/')

  view = customers_list
  response = view(request)

  assert response.status_code == 200
  
  customers = Customer.objects.all()
  serializer = CustomerSerializer(customers, many=True)
  
  assert response.data == serializer.data


@pytest.mark.django_db
def test_order_list(api_client):
  customer = Customer.objects.create(username='alice', code='W2BC5')
  orde1 = Order.objects.create(item="laptop", amount=45000, customer=customer)
  order2 = Order.objects.create(item="bag", amount=1500, customer=customer)
  
  factroy = APIRequestFactory()
  
  request = factroy.get('/orders/')
  view = order_list
  response = view(request)
  
  assert response.status_code == 200
  
  orders = Order.objects.all()
  serializer = OrderSerializer(orders, many=True)
  
  assert response.data == serializer.data