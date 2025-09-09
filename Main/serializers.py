from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['Name','Price','Quantity','Is_Available']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['Products','Total_price']

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['FullName','Username','Password','Email','Cart']