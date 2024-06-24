from rest_framework import serializers

from .models import Restaurant
from .models import CartItem
from .models import Order

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id','title','price','rating','description','completed')

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('id','restaurant','quantity','price')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id','cartItems','grandTotal','totalAmount','gst','deliveryFee')