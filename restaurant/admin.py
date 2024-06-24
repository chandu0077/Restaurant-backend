from django.contrib import admin
from .models import  Restaurant
from .models import  CartItem
from .models import  Order
# Register your models here.

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('title','price','rating','description','completed')

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id','restaurant','quantity','price')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','cartItems','grandTotal','totalAmount','gst','deliveryFee')

admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(CartItem,CartItemAdmin)
admin.site.register(Order,OrderAdmin)