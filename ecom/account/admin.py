from django.contrib import admin
from .models import UserAddress , UserAccount
# Register your models here.

admin.site.register(UserAccount)
admin.site.register(UserAddress)



