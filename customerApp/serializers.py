from rest_framework import serializers
from customerApp.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Customer
    fields = ['id', 'username', 'code']
    
    
    def create(self, validated_data):
      return Customer.objects.create(**validated_data)