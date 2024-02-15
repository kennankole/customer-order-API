from django.shortcuts import render
from rest_framework import permissions, status

from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.response import Response
from customerApp.models import Customer, Order
from customerApp.serializers import CustomerSerializer, OrderSerializer
# Create your views here.

@api_view(['GET'])
# @permission_classes([permissions.AllowAny])
def customers_list(request):
  if request.method == 'GET':
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
@api_view(['GET'])
def order_list(request):
  if request.method == 'GET':
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


