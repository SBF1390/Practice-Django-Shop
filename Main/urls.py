from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("Products", ProductsGenericsApiView.as_view()),
    path("Products/<pk>", ProductsGenericsDetailedView.as_view()),
    path("Products/MostSold", ProductsMostSold.as_view()),
    path("Cart/Create", CartGenericsCApiView.as_view()),
    path("Cart/<pk>", CartGenericsDetailedView.as_view()),
    path("Cart/Today", CartTodaySearch.as_view()),
    path("Member", MemberGenericsApiView.as_view()),
    path("Member/<pk>", MemberGenericsDetailedView.as_view()),
    path("Member/<pk>/orders", MemberGenericsOrders.as_view()),
]
