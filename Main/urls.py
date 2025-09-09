from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("ProductsAPI",ProductsGenericsApiView.as_view()),
    path("ProductsAPI/<pk>",ProductsGenericsDetailedView.as_view()),
    path("CartAPI",CartGenericsApiView.as_view()),
    path("CartAPI/<pk>",CartGenericsDetailedView.as_view()),
    path("MemberAPI",MemberGenericsApiView.as_view()),
    path("MemberAPI/<pk>",MemberGenericsDetailedView.as_view()),
]
