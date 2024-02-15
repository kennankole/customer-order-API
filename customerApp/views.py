from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from customerApp.models import Customer
from customerApp.serializers import CustomerSerializer
# Create your views here.


