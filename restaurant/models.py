from django.db import models

# Create your models here.
class Restaurant(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField(default=0)
    rating = models.DecimalField(default=0,max_digits=2,decimal_places=1)
    description = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class CartItem(models.Model):
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    # restaurant = models.JSONField(default=)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.quantity

class Order(models.Model):

    cartItems=models.TextField(default="")
    grandTotal = models.IntegerField(default=0)
    totalAmount = models.IntegerField(default=0)
    gst = models.IntegerField(default=0)
    deliveryFee = models.IntegerField(default=0)

    def __str__(self):
        return self.grandTotal