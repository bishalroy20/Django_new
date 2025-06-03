from django.urls import path
from . import views

urlpatterns = [
    # path('add/<int:pk>',views.add_to_cart , name='add'),
    # path('cart/<int:user_id>/<int:chk>',views.cart_view , name='cart'),
    # path('remove-item/<int:pk>',views.remove_from_cart , name='remove-item'),
    # path('increase-item/<int:pk>',views.increase_cart , name='increase-item'),
    # path('decrease-item/<int:pk>',views.decrease_cart , name='decrease-item'),


    path('cart/', views.cart_view, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update-cart/<int:cart_item_id>/', views.update_cart, name='update_cart'),
    path('orders/', views.order_summary, name='order_summary'),
]
