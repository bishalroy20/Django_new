from django.db import models
from django.contrib.auth.models import User
from .constants import GENDER_TYPE
# Create your models here.



class UserAccount(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    account_no = models.IntegerField(unique=True) # account no duijon user er kokhono same hobe na
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_TYPE)
    profile_picture = models.ImageField(upload_to='images/', null=True, blank=True)  # Upload field

    def __str__(self):
        return f"Account No: {self.account_no}"

    


class UserAddress(models.Model):
    user = models.OneToOneField(User, related_name='address', on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length= 100)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=100)
    def __str__(self):
        return str(self.user.email)