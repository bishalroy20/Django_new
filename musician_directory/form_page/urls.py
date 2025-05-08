from django.urls import path , include
from . import views

urlpatterns = [
    path('add_author/' , views.add_author , name='add_author'),
    path('edit_author/<int:id>/' ,views.edit_author , name='edit_author'),
]


