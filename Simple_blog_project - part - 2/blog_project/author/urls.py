from django.urls import path , include
from . import views

urlpatterns = [
    path('register/',views.register , name = 'register'),
    path('login/',views.user_login , name = 'login'),
    path('profile/',views.profile , name = 'profile'),
    path('',views.user_logout , name = 'logout'),
    path('profile/edit/',views.edit_profile , name = 'edit_profile'),
    path('profile/edit/pass_change/',views.pass_change , name = 'pass_change'),

]

