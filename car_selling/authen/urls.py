from django.urls import path , include
from . import views

urlpatterns = [
    path('signup/' , views.register , name = 'register'),
    path('login/' , views.user_login , name = 'login'),
    path('logout/' , views.user_logout , name = 'logout'),
    path('profile/' , views.profile , name = 'profile'),
    path('edit_profile/' , views.edit_profile , name = 'edit_profile'),
]