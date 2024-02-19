from rest_framework import serializers
from customerApp.models import Customer, Order

class CustomerSerializer(serializers.ModelSerializer):
  orders = serializers.PrimaryKeyRelatedField(many=True, queryset=Order.objects.all())
  
  class Meta:
    model = Customer
    fields = ['username', 'password', 'code', 'orders']
    
    def create(self, validated_data):
      return Customer.objects.create(**validated_data)
    
class OrderSerializer(serializers.ModelSerializer):
  owner = serializers.ReadOnlyField(source='owner.username')
  class Meta:
    model = Order
    fields = '__all__'
    
  def create(self, validated_data):
    return Order.objects.create(**validated_data)