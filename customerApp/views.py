from django.shortcuts import render
from rest_framework import permissions, status

from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.response import Response
from customerApp.models import Customer, Order
from customerApp.serializers import CustomerSerializer, OrderSerializer
from rest_framework.parsers import JSONParser
# Create your views here.


@api_view(['GET', 'POST'])
@permission_classes([permissions.AllowAny])
def customers_list(request, format=None):
  if request.method == 'GET':
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)
  
  elif request.method == 'POST':
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(["GET", "POST"])
def customer_detail(request, pk, format=None):
  try:
    customer = Customer.objects.get(pk=pk)
  except Customer.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    serializer = CustomerSerializer(customer)
    return Response(serializer.data)
  
  elif request.method == 'POST':
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save(customer=customer)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  

@api_view(['GET'])
def order_list(request, format=None):
  if request.method == 'GET':
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


