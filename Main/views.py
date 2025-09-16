from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from .models import *
from .serializers import *
from datetime import date


class ProductsGenericsApiView(generics.ListCreateAPIView):
    queryset = Products.objects.order_by("id").all()
    serializer_class = ProductSerializer


class ProductsGenericsDetailedView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.order_by("id").all()
    serializer_class = ProductSerializer

class ProductsMostSold(generics.ListAPIView):
    queryset = Products.objects.order_by("-Sold").all()
    serializer_class = ProductSerializer

class MemberGenericsApiView(generics.ListCreateAPIView):
    queryset = Products.objects.order_by("id").all()
    serializer_class = MemberSerializer


class MemberGenericsDetailedView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.order_by("id").all()
    serializer_class = MemberSerializer


class CartGenericsCApiView(generics.CreateAPIView):
    queryset = Products.objects.order_by("id").all()
    serializer_class = CartSerializer

    def perform_create(self, serializer):
        cart_instance = serializer.save()
        Products = cart_instance.Products
        Products.Quantity -= cart_instance.Quantity
        Products.save()


class CartGenericsDetailedView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.order_by("id").all()
    serializer_class = CartSerializer


class CartTodaySearch(generics.ListAPIView):
    queryset = Cart.objects.all()

    def get_queryset(self):
        return Cart.objects.filter(Date=date.today)


class MemberGenericsOrders(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_queryset(self):
        user_pk = self.kwargs.get("pk")
        if user_pk:
            return self.queryset.filter(id=user_pk)
        else:
            return self.queryset.none()
