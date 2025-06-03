from django.db import models
from category.models import Sport
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    image = models.ImageField(upload_to='images/' , blank=True , null= True )
    name = models.CharField(max_length=100)
    sport_name = models.ForeignKey(Sport, on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.TextField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-price',]
    

class comment(models.Model):
    car = models.ForeignKey(Product , on_delete= models.CASCADE , related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"commented by {{self.name}}"
