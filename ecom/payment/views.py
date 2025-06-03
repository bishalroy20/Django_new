from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from django.conf import settings
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt 
from sslcommerz_lib import SSLCOMMERZ
import uuid
from cart.models import Cart, Order
from django.contrib.auth.mixins import LoginRequiredMixin


class OrderHistoryView(LoginRequiredMixin, View):
    def get(self, request):
        # Get all orders for the logged-in user
        orders = Order.objects.filter(user=request.user).order_by('-created_at')

        context = {
            'orders': orders
        }
        return render(request, 'order_history.html', context)






@method_decorator(login_required, name='dispatch')  # Ensure the user is logged in
@method_decorator(csrf_exempt, name='dispatch')     # Exempt csrf for the payment process
class CreatePaymentSessionView(View):
    def post(self, request, *args, **kwargs):
        return self._process_payment(request)
    
    def get(self, request, *args, **kwargs):
        return self._process_payment(request)

    
    def _process_payment(self, request):
        sslcz = SSLCOMMERZ(settings.SSLCOMMERZ_SETTINGS)

        # DEBUG: print current user
        print("Logged-in user:", request.user)
        transaction_id = str(uuid.uuid4().hex)[:10]
        # DEBUG: fetch cart items
        cart_items = Cart.objects.filter(user=request.user, purchased=False)
        print("Cart items found:", cart_items.count())

        for item in cart_items:
            print(f"Item: {item.product.name}, Quantity: {item.quantity}, Purchased: {item.purchased}")

        # If no items in the cart
        if not cart_items.exists():
            return HttpResponse("Your cart is empty. Please add items to the cart.")

        order_items = cart_items  # No need for list comprehension here

        # Calculate the total price
        total_price = sum(item.product.price * item.quantity for item in order_items)

        # Build absolute URLs for success, fail, and cancel pages
        success_url = request.build_absolute_uri('/payment/success/')
        fail_url = request.build_absolute_uri('/payment/fail/')
        cancel_url = request.build_absolute_uri('/payment/cancel/')

        # Create the post_body for SSLCOMMERZ
        post_body = {
            'total_amount': total_price,
            'currency': "BDT",
            'tran_id': transaction_id,
            'success_url': success_url,
            'fail_url': fail_url,
            'cancel_url': cancel_url,
            'emi_option': 0,
            'cus_name': request.user.username,
            'cus_email': request.user.email,
            'cus_phone': "01700000000",  # Optionally, you can get the user's phone
            'cus_add1': "Customer Address",  # Get from user profile or checkout form
            'cus_city': "Dhaka",
            'cus_country': "Bangladesh",
            'shipping_method': "NO",
            'multi_card_name': "",
            'num_of_item': len(order_items),
            'product_name': "Test Product",  # Optionally, use actual product names from the cart
            'product_category': "General",
            'product_profile': "general"
        }

        try:
            # Create session with SSLCOMMERZ
            response = sslcz.createSession(post_body)

            # Debug: Print response
            print("SSLCOMMERZ Response:", response)

            # Check if the response contains the necessary 'GatewayPageURL'
            if 'GatewayPageURL' in response:
                # Create an order in the database
                order = Order.objects.create(
                    user=request.user,
                    order_id=transaction_id,
                    payment_id=response.get('tran_id', '')  # Safely handle 'tran_id'
                )
                order.order_items.set(order_items)
                order.save()

                # Mark the cart items as purchased (so they are not included in future payments)
                cart_items.update(purchased=True)

                # Redirect the user to SSLCOMMERZ payment gateway
                return redirect(response['GatewayPageURL'])
            else:
                return HttpResponse("Payment initialization failed! Please try again. Error: " + str(response))
        except Exception as e:
            return HttpResponse(f"Error: {str(e)}")




@method_decorator(csrf_exempt, name='dispatch')
class PaymentSuccessView(TemplateView):
    template_name = 'success.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get data from either GET or POST depending on how the gateway redirected
        data = self.request.GET.dict() if self.request.GET else self.request.POST.dict()
        
        # Process and clean up the payment data
        payment_info = {
            'transaction_id': data.get('tran_id', ''),
            'amount': data.get('amount', ''),
            'currency': data.get('currency', 'BDT'),
            'card_type': data.get('card_type', ''),
            'payment_status': data.get('status', 'VALID'),
            'bank_transaction_id': data.get('bank_tran_id', ''),
            'validation_id': data.get('val_id', ''),
            'transaction_date': data.get('tran_date', ''),
            'card_issuer': data.get('card_issuer', ''),
            'card_brand': data.get('card_brand', ''),
            'card_issuer_country': data.get('card_issuer_country', ''),
            'store_amount': data.get('store_amount', ''),
        }
        
        # Add both raw data and processed data to context
        context['payment_data'] = data
        context['payment_info'] = payment_info
        return context
        
    def post(self, request, *args, **kwargs):
        # Handle POST requests from payment gateway
        return self.render_to_response(self.get_context_data(**kwargs))



@method_decorator(csrf_exempt, name='dispatch')
class PaymentFailView(TemplateView):
    template_name = 'fail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['payment_data'] = self.request.GET
        return context
        
    def post(self, request, *args, **kwargs):
        # Handle POST requests from payment gateway
        context = self.get_context_data(**kwargs)
        context['payment_data'] = request.POST
        return self.render_to_response(context)



@method_decorator(csrf_exempt, name='dispatch')
class PaymentCancelView(TemplateView):
    template_name = 'cancel.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['payment_data'] = self.request.GET
        return context
        
    def post(self, request, *args, **kwargs):
        # Handle POST requests from payment gateway
        context = self.get_context_data(**kwargs)
        context['payment_data'] = request.POST
        return self.render_to_response(context)




@method_decorator(csrf_exempt, name='dispatch')
class IPNHandlerView(View):
    def post(self, request, *args, **kwargs):
        sslcz = SSLCOMMERZ(settings.SSLCOMMERZ_SETTINGS)
        post_body = request.POST.dict()
        
        try:
            if sslcz.hash_validate_ipn(post_body):
                response = sslcz.validationTransactionOrder(post_body['val_id'])
                print("Transaction Validated:", response)
                return HttpResponse("IPN Validation Successful")
            else:
                print("Hash validation failed")
                return HttpResponse("IPN Validation Failed")
        except Exception as e:
            print(f"IPN Error: {str(e)}")
            return HttpResponse(f"IPN Error: {str(e)}")
            
    def get(self, request, *args, **kwargs):
        return HttpResponse("Invalid Request")