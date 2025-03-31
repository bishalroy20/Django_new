from django.urls import path , include
from . import views

urlpatterns = [
    path('register/' , views.register , name='register'),
    path('login/' , views.user_login , name='login'),
    path('profile/' , views.profile , name='profile'),
    path('' , views.user_logout , name='logout'),
    path('add_author/' , views.add_author , name='add_author'),
    path('edit_author/<int:id>/' ,views.edit_author , name='edit_author'),
]


