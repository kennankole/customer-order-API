from rest_framework import serializers
from customerApp.models import Customer, Order

class CustomerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Customer
    fields = ['id', 'username', 'code']
    
    
    def create(self, validated_data):
      return Customer.objects.create(**validated_data)
    
    
class OrderSerializer(serializers.ModelSerializer):
  class Meta:
    model = Order
    fields = ['id', 'item', 'amount']
    
  def create(self, validated_data):
    return Order.objects.create(**validated_data)