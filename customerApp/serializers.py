from rest_framework import serializers
from django.contrib.auth import get_user_model
from customerApp.models import Customer, Order    

Customer = get_user_model()
class OrderSerializer(serializers.ModelSerializer):
  owner = serializers.ReadOnlyField(source='owner.username')
  class Meta:
    model = Order
    fields = '__all__'
    
  def create(self, validated_data):
    return Order.objects.create(**validated_data)
  

class CustomerSerializer(serializers.ModelSerializer):
  orders = OrderSerializer(many=True, read_only=True)
  
  class Meta:
    model = Customer
    fields = ('username', 'password', 'phone_number', 'customer_code', 'orders')
    read_only_fields = ('orders', )
          
    def create(self, validated_data):
      return Customer.objects.create_user(**validated_data)