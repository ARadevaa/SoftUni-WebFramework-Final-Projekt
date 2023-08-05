from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from grocery_store.order.models import Order, OrderedItems
from grocery_store.product.models import Product


@login_required
def place_order(request):
    if request.method == 'POST':
        cart_items = request.session.get('cart_items', [])

        if not cart_items:
            return redirect('view_cart')

        # Create the Order instance and associate it with the user's cart
        order = Order.objects.create(user=request.user)

        # Move cart items to OrderedItems and associate them with the Order
        for cart_item in cart_items:
            product_id = cart_item.get('product_id')
            quantity = cart_item.get('quantity', 0)

            if product_id and quantity:
                product = get_object_or_404(Product, id=product_id)

                ordered_item = OrderedItems.objects.create(
                    user=request.user,
                    product=product,
                    quantity=quantity,
                )
                order.items.add(ordered_item)  # Associate the OrderedItem with the Order

        # Clear the cart items from the session after the order is placed
        del request.session['cart_items']

        # Redirect to the order confirmation page with the order_id
        return redirect('order_confirmation', order_id=order.id)
    else:
        return redirect('view_cart')


@login_required()
def order_history(request):
    # Get all orders for the logged-in user
    orders = Order.objects.filter(user=request.user)

    # You can use the 'orders' queryset to display order history in the template
    context = {
        'orders': orders,
    }
    return render(request, 'order/order_history.html', context)


@login_required
def order_confirmation(request, order_id):
    # Get the order object based on the order_id
    try:
        order = Order.objects.get(id=order_id)
        items = order.items.all()
        total_order_cost = 0
        for item in items:
            total_order_cost += item.total_price

    except Order.DoesNotExist:
        raise Http404("Order not found")

    context = {
        'order': order,
        'items': items,
        'total_order_cost': total_order_cost,
    }
    return render(request, 'order/order_confirmation.html', context)


def all_orders(request):

    all_orders = Order.objects.all()

    context = {
        'all_orders': all_orders
    }

    return render(request, 'order/all_orders.html', context)
