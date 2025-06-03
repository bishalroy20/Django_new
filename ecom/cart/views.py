from django.shortcuts import render , redirect , get_object_or_404
from .models import Cart , Order , OrderItem
from product.models import Product
from cart.models import Cart 
from django.views.decorators.csrf import csrf_exempt 
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required



def cart_view(request):
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
    else:
        cart_items = Cart.objects.filter(session_id=request.session.session_key)

    grand_total = sum(item.product.price * item.quantity for item in cart_items)

    return render(request, 'cart.html', {'cart_items': cart_items, 'grand_total': grand_total})



def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    
    if request.user.is_authenticated:
        cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    else:
        session_id = request.session.session_key or request.session.create()
        cart_item, created = Cart.objects.get_or_create(session_id=session_id, product=product)

    if not created:
        cart_item.quantity += 1
    cart_item.save()

    return redirect('cart')


def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id)

    # Ensure only the owner can remove items
    if request.user.is_authenticated:
        if cart_item.user == request.user:
            cart_item.delete()
    else:
        if cart_item.session_id == request.session.session_key:
            cart_item.delete()

    return redirect('cart')


def update_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id)
    
    if request.user.is_authenticated and cart_item.user == request.user:
        if request.POST['action'] == 'increase':
            cart_item.quantity += 1
        elif request.POST['action'] == 'decrease' and cart_item.quantity > 1:
            cart_item.quantity -= 1
        cart_item.save()

    return redirect('cart')


def order_summary(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, "order_history.html", {"orders": orders})



# @login_required
# def add_to_cart(request , pk):
#     item = get_object_or_404(Product , pk = pk)
#     order_item =Cart.objects.get_or_create(item = item , user=request.user , purchased = False)
#     order_qs = Order.objects.filter(user = request.user , ordered = False)
#     if order_qs.exists():
#         order = order_qs[0]
#         if order.orderitems.filter(item=item).exists():
#             order_item[0].quantity += 1
#             order_item[0].save()
#             messages.info(request , "This item quantity was updated!")
#             return redirect('home')
#         else:
#             order.orderitems.add(order_item[0])
#             messages.info(request , "This item was added to your cart")
#             return redirect('home')
    
#     else:
#         order = Order(user= request.user)
#         order.save()
#         order.orderitems.add(order_item[0])
#         messages.info(request , "This item was added to your cart")
#         return redirect('home')


# @csrf_exempt
# def cart_view(request, user_id , chk):
#     print('\n=====================================')
#     print('cart_view_called')
#     print(request.user)
#     print('========================================')
#     user = User.objects.get(id=user_id)
#     if chk ==0:
#         messages.warning(request , "your payment was not completed")
    
#     carts = Cart.objects.filter(user=user , purchased=False)
#     orders = Order.objects.filter(user=user , ordered = False)
    
#     if carts.exists() and orders.exists():
#         order = orders[0]
#         context = {
#             'carts' : carts,
#             'order' : order 
#         }
#         return render(request , 'cart.html' , context)
#     else:
#         messages.warning(request , "You donot have any item in your cart")
#         return redirect('home')


# @login_required
# def remove_from_cart(request , pk):
#     item = get_object_or_404(Product , pk = pk)
#     order_qs = Order.objects.filter(user = request.user , ordered = False)
#     if order_qs.exists():
#         order = order_qs[0]
#         if order.orderitems.filter(item=item).exists():
#             order_item = Cart.objects.filter(item=item , user=request.user , purchased = False)[0]
#             order.orderitems.remove(order_item)
#             order_item.delete()
#             messages.warning(request , "This item was removed from your cart!")
#             return redirect('cart' ,request.user.id,1)
        
#         else:
#             messages.info(request , "This item was not in your cart")
#             return redirect('home')
    
#     else:
#         messages.info(request , "You don't have an active order")
#         return redirect('home')
    

# @login_required
# def increase_cart(request , pk):
#     item = get_object_or_404(Product , pk = pk)
#     order_qs = Order.objects.filter(user = request.user , ordered = False)
#     if order_qs.exists():
#         order = order_qs[0]
#         if order.orderitems.filter(item=item).exists():
#             order_item = Cart.objects.filter(item=item , user=request.user , purchased = False)[0]
#             if order_item.quantity >= 1:
#                 order_item.quantity += 1
#                 order_item.save()
#                 messages.warning(request , f"{item.name} quantity has been updated")
#                 return redirect('cart' ,request.user.id,1)
#         else:
#             messages.info(request , f"{item.name} is not in your cart")
#             return redirect('home')
        
#     else:
#         messages.info(request , "You don't have an active order")
#         return redirect('home')




# @login_required
# def decrease_cart(request , pk):
    item = get_object_or_404(Product , pk = pk)
    order_qs = Order.objects.filter(user = request.user , ordered = False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item , user=request.user , purchased = False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                messages.warning(request , f"{item.name} quantity has been updated")
                return redirect('cart' ,request.user.id,1)
        else:
            messages.info(request , f"{item.name} is not in your cart")
            return redirect('home')
        
    else:
        messages.info(request , "You don't have an active order")
        return redirect('home')
    

