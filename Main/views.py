from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import status
from .models import *
from .serializers import *

class ProductsGenericsApiView(generics.ListCreateAPIView):
    queryset = Products.objects.order_by('id').all()
    serializer_class = ProductSerializer

class ProductsGenericsDetailedView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.order_by('id').all()
    serializer_class = ProductSerializer

class CartGenericsApiView(generics.ListCreateAPIView):
    queryset = Products.objects.order_by('id').all()
    serializer_class = CartSerializer

class CartGenericsDetailedView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.order_by('id').all()
    serializer_class = CartSerializer

class MemberGenericsApiView(generics.ListCreateAPIView):
    queryset = Products.objects.order_by('id').all()
    serializer_class = MemberSerializer
class MemberGenericsDetailedView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.order_by('id').all()
    serializer_class = MemberSerializer