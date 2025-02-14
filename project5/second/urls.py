from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.contact , name = 'contact'),
    path('about/', views.about  , name = 'about'),
    path('form/', views.form  , name = 'form'),
    path('django_form/', views.Django_form  , name = 'django_form'),
]
