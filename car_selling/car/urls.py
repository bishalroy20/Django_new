from django.urls import path , include
from . import views

urlpatterns = [
    path('add_car/' , views.AddCarView.as_view() , name= 'add_car'),
    path('edit_car/<int:id>/' , views.EditCarView.as_view() , name= 'edit_car'),
    
]

