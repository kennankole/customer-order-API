from rest_framework import permissions, viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from django.contrib.auth import get_user_model

from customerApp.models import Customer, Order
from customerApp.serializers import CustomerSerializer, OrderSerializer

Customer = get_user_model()

class CustomerViewSet(viewsets.ModelViewSet):
  queryset = Customer.objects.all()
  serializer_class = CustomerSerializer
  permission_classes = [permissions.IsAuthenticated]
  
class OrderViewSet(viewsets.ModelViewSet):
  queryset = Order.objects.all()
  serializer_class = OrderSerializer
  permission_classes = [permissions.IsAuthenticated]
  
  def perform_create(self, serializer):
    return serializer.save(owner=self.request.user)

  
class CustomerLogIn(ObtainAuthToken):
  def post(self, request, *args, **kwargs):
    serializer = self.serializer_class(
      data=request.data,
      context={
        'request': request
      }
    )
    serializer.is_valid(raise_exception=True)
    customer = serializer.validated_data["user"]
    token = Token.objects.get(user=customer)
    return Response({
      'token': token.key,
      'id': customer.pk,
      'username': customer.username,
      'customer_code': customer.customer_code
    })