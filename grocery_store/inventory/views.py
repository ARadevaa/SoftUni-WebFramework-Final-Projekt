from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.timezone import now


from grocery_store.categories.models import Category
from grocery_store.common.forms import SearchForm
from grocery_store.inventory.decorators import group_required
from grocery_store.inventory.forms import DeliveryAddForm
from grocery_store.inventory.models import Report, Delivery
from grocery_store.order.models import Order
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
@group_required('Staff')
def inventory_details(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    promo_products = Promo.objects.all()
    search_form = SearchForm(request.GET)
    all_orders = Order.objects.all()

    if search_form.is_valid():
        search_text = search_form.cleaned_data['search_text']
        products = products.filter(name__icontains=search_text)

    context = {
        "all_products": products,
        "all_categories": categories,
        "promo_products": promo_products,
        "search_form": search_form,
        "all_orders": all_orders
    }
    return render(request, 'inventory/inventory-details-page.html', context)


def delivery_report(request):
    all_deliveries = Delivery.objects.all()

    context = {
        'all_deliveries': all_deliveries
    }

    return render(request, 'inventory/delivery_report.html', context)
