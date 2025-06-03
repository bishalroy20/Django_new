from django.urls import path
from .views import (
     
    CreatePaymentSessionView, 
    PaymentSuccessView, 
    PaymentFailView, 
    PaymentCancelView, 
    IPNHandlerView,
    OrderHistoryView
)

urlpatterns = [
    path('create-payment/', CreatePaymentSessionView.as_view(), name='create_payment'),
    path('payment/success/', PaymentSuccessView.as_view(), name='payment_success'),
    path('payment/fail/', PaymentFailView.as_view(), name='payment_fail'),
    path('payment/cancel/', PaymentCancelView.as_view(), name='payment_cancel'),
    path('payment/ipn/', IPNHandlerView.as_view(), name='ipn_handler'),
    path('order-history/', OrderHistoryView.as_view(), name='order_history'),
]