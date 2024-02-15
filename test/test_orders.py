import pytest
from rest_framework.test import APIRequestFactory, APIClient
from customerApp.views import customers_list
from customerApp.serializers import CustomerSerializer
from customerApp.models import Customer

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
