from rest_framework import  generics, permissions
from customerApp.models import Customer, Order
from customerApp.serializers import CustomerSerializer, OrderSerializer

class IsCustomerCreationOrAuthenticated(permissions.BasePermission):
  def has_permission(self, request, view):
    if request.method == 'POST':
      return True
    return request.user and request.user.is_authenticated
class OrderList(generics.ListCreateAPIView):
  queryset = Order.objects.all()
  serializer_class = OrderSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  
  def perform_create(self, serializer):
    return serializer.save(owner=self.request.user)
  
class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Order.objects.all()
  serializer_class = OrderSerializer
  permission_classes = [permissions.IsAuthenticated]
  
class CustomerList(generics.ListCreateAPIView):
  queryset = Customer.objects.all()
  serializer_class = CustomerSerializer
  permission_classes = [IsCustomerCreationOrAuthenticated]
  
class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Customer.objects.all()
  serializer_class = CustomerSerializer
  permission_classes = [permissions.IsAuthenticated]