from django.urls import path
from . import views
urlpatterns = [
    path('', views.home , name="home"),
    path('modelform/', views.home2 , name="home2"),
]