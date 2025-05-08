from django.shortcuts import render , redirect , get_object_or_404
from .models import Cart
from product.models import Product


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