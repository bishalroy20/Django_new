from django.urls import path , include
from . import views

urlpatterns = [
    path('' , views.signup , name='signup'),
    path('login/' , views.user_login , name='login'),
    path('profile/' , views.profile , name='profile'),
    path('logout/' , views.user_logout , name='logout'),
    path('pass_change/' , views.pass_change , name='pass_change'),
    path('pass_change2/' , views.pass_change2 , name='pass_change2'),
]