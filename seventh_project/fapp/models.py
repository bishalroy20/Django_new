from django.db import models

# Create your models here.
class studentmodel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    fathers_name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)