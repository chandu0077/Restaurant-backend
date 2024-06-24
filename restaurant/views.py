from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RestaurantSerializer
from .serializers import CartItemSerializer
from .serializers import OrderSerializer
from .models import Restaurant
from .models import CartItem
from .models import Order

class RestaurantView(viewsets.ModelViewSet):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()


class CartItemView(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()

class OrderView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
# Create your views here.
