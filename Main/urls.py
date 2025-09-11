from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("Products",ProductsGenericsApiView.as_view()),
    path("Products/<pk>",ProductsGenericsDetailedView.as_view()),
    path("Cart",CartGenericsApiView.as_view()),
    path("Cart/<pk>",CartGenericsDetailedView.as_view()),
    path("Member",MemberGenericsApiView.as_view()),
    path("Member/<pk>",MemberGenericsDetailedView.as_view()),
]
