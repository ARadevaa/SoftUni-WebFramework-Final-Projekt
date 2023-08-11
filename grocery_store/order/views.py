from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

from grocery_store.order.forms import SearchForm
from grocery_store.order.models import Order, OrderedItems
from grocery_store.product.models import Product


@login_required
def place_order(request):
    if request.method == 'POST':
        cart_items = request.session.get('cart_items', [])

        if not cart_items:
            return redirect('view_cart')

        order = Order.objects.create(user=request.user)

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
                order.items.add(ordered_item)

        request.session['cart_items'] = []

        return redirect('order_confirmation', order_id=order.id)
    else:
        return redirect('view_cart')


@login_required()
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    context = {
        'orders': orders,
    }
    return render(request, 'order/order_history.html', context)


@login_required
def order_confirmation(request, order_id):
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


@login_required
def order_list(request,):
    orders = Order.objects.all().order_by('-created_at')

    search_form = SearchForm(request.GET)

    if search_form.is_valid():
        search_text = search_form.cleaned_data['search_text']
        orders = orders.filter(status__icontains=search_text)

    context = {
        'orders': orders,
        'status_choices': Order.STATUS_CHOICES,
        "search_form": search_form,
    }
    return render(request, 'order/all_orders_history.html', context)


@login_required
def update_order_status(request, pk):
    order = get_object_or_404(Order, pk=pk)

    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(Order.STATUS_CHOICES).keys():
            order.status = new_status
            order.save()
            return redirect('all_orders')

    context = {
        'order': order,
    }
    return render(request, 'order/order_status_update.html', context)
