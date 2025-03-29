from django.urls import path , include
from . import views
urlpatterns = [
    path('' , views.signup , name='signup'),
    path('login/' , views.user_login , name='login'),
    path('profile/' , views.profile , name='profile'),
    path('logout/' , views.user_logout , name='logout'),
    path('pass_change1/' , views.pass_change , name='passchange1'),
    path('passchange2/' , views.pass_change2 , name='passchange2'),

]