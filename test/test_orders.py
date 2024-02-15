import pytest
from django.urls import reverse
from pytest_drf import APIViewTest, Returns200, UsesGetMethod

class TestOrders(APIViewTest, UsesGetMethod, Returns200):
  @pytest.fixture
  def url(self):
    return reverse('orders')
  
  def test_it_returns_all_orders(self, json):
    excepted = 'All orders'
    actual = json
    assert excepted == actual