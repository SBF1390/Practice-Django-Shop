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


class MemberGenericsApiView(generics.ListCreateAPIView):
    queryset = Products.objects.order_by('id').all()
    serializer_class = MemberSerializer
class MemberGenericsDetailedView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.order_by('id').all()
    serializer_class = MemberSerializer
class CartGenericsCApiView(generics.CreateAPIView):
    queryset = Products.objects.order_by('id').all()
    serializer_class = CartSerializer

    def perform_create(self, serializer):
        cart_instance = serializer.save()
        Products = cart_instance.Products
        Products.Quantity -= cart_instance.Quantity
        Products.save()

class CartGenericsDetailedView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.order_by('id').all()
    serializer_class = CartSerializer