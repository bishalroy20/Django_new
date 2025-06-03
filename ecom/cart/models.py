from django.db import models
from django.contrib.auth.models import User
from product.models import Product
import datetime

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    session_id = models.CharField(max_length=100, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    purchased = models.BooleanField(default=False)


# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     order_items = models.ManyToManyField(Cart)  # Stores cart products
#     ordered = models.BooleanField(default=False)  # Payment status
#     payment_id = models.CharField(max_length=255, blank=True, null=True)  # Transaction ID
#     order_id = models.CharField(max_length=255, blank=True, null=True)  # Unique Order ID
#     created_at = models.DateTimeField(auto_now_add=True)  # Order timestamp

#     def get_total_price(self):
#         return sum(item.get_total() for item in self.order_items.all())

#     def __str__(self):
#         return f"Order {self.order_id} - {self.user.username}"



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # order_id = models.CharField(max_length=100, unique=True)
    payment_id = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="Pending")  # e.g., Pending, Completed

    def __str__(self):
        return f"Order {self.order_id} by {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"
  
    

    
