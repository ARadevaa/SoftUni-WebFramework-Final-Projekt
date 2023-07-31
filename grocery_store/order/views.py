from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from grocery_store.cart.models import Cart
from grocery_store.order.models import Order


@login_required
def place_order(request):
    if request.method == 'POST':
        user_cart = Cart.objects.filter(user=request.user)  # Change this if using AnonymousUser

        if not user_cart.exists():
            # Handle empty cart; redirect to view_cart or show an error message
            return redirect('view_cart')

        # Create a new order for the user
        order = Order.objects.create(user=request.user, cart=user_cart.first())

        # Set the order status to 'Pending' (you can set any initial status you prefer)
        order.status = 'Pending'
        order.save()

        # Optionally, you can add other order-related logic here, such as sending order confirmation emails

        # Clear the user's cart after the order is placed
        user_cart.delete()

        # Redirect to a page that shows the order confirmation or order history
        return redirect('order_confirmation', order_id=order.pk)  # Replace 'order_confirmation' with the URL name of the order confirmation page
    else:
        return redirect('order_confirmation')  # Redirect to the cart if the request method is not POST


@login_required()
def order_history(request):
    if not request.user.is_authenticated:
        # Redirect to the login page or handle anonymous users as needed
        return redirect('login')
    # Retrieve all orders for the current user
    user_orders = Order.objects.filter(user=request.user)

    return render(request, 'order/order_history.html', {'orders': user_orders})


@login_required
def order_confirmation(request, order_id):
    # Retrieve the order using the provided order_id
    order = get_object_or_404(Order, pk=order_id)

    return render(request, 'order/order_confirmation.html', {'order': order})
