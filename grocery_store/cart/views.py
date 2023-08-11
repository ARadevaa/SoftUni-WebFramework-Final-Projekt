from django.contrib.auth.decorators import login_required
from django.contrib.messages import error, success
from django.shortcuts import  get_object_or_404
from django.shortcuts import render, redirect
from grocery_store.product.models import Product


@login_required
def add_to_cart(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    quantity = int(request.POST.get('quantity', 1))

    available_quantity = product.available_quantity

    if quantity <= 0:
        error(request, 'Invalid quantity.')
        return redirect('category details')

    if quantity > available_quantity:
        error(request, 'Requested quantity exceeds available quantity.')
        return redirect('category details')

    cart_items = request.session.get('cart_items', [])

    if not isinstance(cart_items, list):
        # If cart_items is not a list, create an empty list
        cart_items = []

    # Check if the product is already in the cart
    for item in cart_items:
        if item['product_id'] == product.id:
            item['quantity'] += quantity
            break
    else:
        cart_items.append({'product_id': product.id, 'quantity': quantity})

    request.session['cart_items'] = cart_items  # Save the updated cart items to the session

    success(request, 'Product added to cart.')
    return redirect('category details')


def remove_from_cart(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    quantity = int(request.POST.get('quantity', 1))
    cart_items = request.session.get('cart_items', [])
    cart_items.remove({'product_id': product.id, 'quantity': quantity})
    request.session['cart_items'] = cart_items
    request.session.modified = True
    return redirect('view_cart')

@login_required
def view_cart(request):
    cart_items = request.session.get('cart_items', [])

    total_order_cost = 0
    for cart_item in cart_items:
        product_id = cart_item.get('product_id')
        quantity = cart_item.get('quantity', 0)
        product = get_object_or_404(Product, id=product_id)
        cart_item['product'] = product
        cart_item['total_price'] = product.price * quantity
        total_order_cost += cart_item['total_price']

    context = {
        'cart_items': cart_items,
        'total_order_cost': total_order_cost,
    }
    return render(request, 'cart/view_cart.html', context)

