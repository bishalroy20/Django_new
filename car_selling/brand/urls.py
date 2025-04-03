from django.urls import path , include
from . import views

urlpatterns = [
    path('add_brand/' , views.add_brand , name= 'add_brand'),
    # path('edit_brand/<int:id>' , views.edit_brand , name='edit_brand'),

]