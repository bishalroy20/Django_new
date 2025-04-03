from django.db import models
from brand.models import Brand
from django.contrib.auth.models import User
# Create your models here.


class Car(models.Model):
    image = models.ImageField(upload_to='images/' , blank=True , null= True )
    name = models.CharField(max_length=100)
    brand_name = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.TextField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
    

class comment(models.Model):
    car = models.ForeignKey(Car , on_delete= models.CASCADE , related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"commented by {{self.name}}"
    

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_purchased = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} bought {self.car.name}"