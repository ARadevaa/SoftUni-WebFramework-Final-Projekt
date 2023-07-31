from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.timezone import now

from grocery_store.cart.models import Cart
from grocery_store.categories.models import Category
from grocery_store.inventory.forms import DeliveryAddForm
from grocery_store.inventory.models import Report, Delivery
from grocery_store.product.models import Product, Promo


# Create your views here.
def delivery_add(request):
    form = DeliveryAddForm()

    if request.method == 'POST':
        form = DeliveryAddForm(request.POST)
        if form.is_valid():
            delivery = form.save(commit=False)
            delivery.delivery_date = now().date()

            product = form.cleaned_data['product']
            quantity_delivered = form.cleaned_data['quantity']
            product.available_quantity += quantity_delivered
            product.save()

            delivery.save()

            return redirect('delivery add')  # to replace web success url

    else:
        form = DeliveryAddForm()

    context = {
        "form": form,
    }
    return render(request, 'inventory/inventory-delivery-page.html', context)


@login_required
def inventory_details(request):
    categories = Category.objects.all()
    cart_items = Cart.objects.filter(user=request.user)
    total_order_cost = sum(cart_item.total_price for cart_item in cart_items)
    products = Product.objects.all()
    promo_products = Promo.objects.all()

    context = {
        "all_products": products,
        "all_categories": categories,
        "promo_products": promo_products,
        "cart_items": cart_items,
        "total_order_cost": total_order_cost
    }
    return render(request, 'inventory/inventory-details-page.html', context)


def delivery_report(request):
    reports = Delivery.objects.all()
    context = {
        'reports': reports
    }

    return render(request, 'inventory/delivery_report.html', context)
