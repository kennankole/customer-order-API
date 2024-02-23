from rest_framework import permissions, viewsets
from rest_framework.authtoken.models import Token

from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.response import Response

from customerApp.models import Customer, Order
from customerApp.serializers import CustomerSerializer, OrderSerializer

from customerApp import utils

Customer = get_user_model()

class IsOwner(permissions.BasePermission):
  def has_permission(self, request, view):
    return request.user.is_authenticated

  def has_object_permission(self, request, view, obj):
    return obj.owner == request.user

class HasTokenPermission(permissions.BasePermission):
  def has_permission(self, request, view):
    token = Token.objects.get(user_id=request.user.id)
    return request.user and request.user.is_authenticated and token.key
class CustomerViewSet(viewsets.ModelViewSet):
  queryset = Customer.objects.all()
  serializer_class = CustomerSerializer
  permission_classes = [permissions.AllowAny]
  
  def get_queryset(self):
    user = self.request.user
    if user.is_authenticated:
      return Customer.objects.filter(pk=user.pk)
    else:
      return Customer.objects.none()
  
  def perform_create(self, serializer):
    user_instance = serializer.save()
    user_instance.set_password(self.request.data['password'])
    user_instance.save()
    return Response(serializer.data, status=status.HTTP_200_OK)
    
class OrderViewSet(viewsets.ModelViewSet):
  queryset = Order.objects.all()
  serializer_class = OrderSerializer
  permission_classes = [permissions.IsAuthenticated, HasTokenPermission, IsOwner]
  
  def perform_create(self, serializer):
    order = serializer.save(owner=self.request.user)
    customer_phone_number = order.customer.phone_number
    utils.SMS().send_message(customer_phone_number)
