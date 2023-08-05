from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from decimal import Decimal

from unicodedata import decimal

from grocery_store.categories.models import Category
from grocery_store.product.forms import ProductAddForm
from grocery_store.product.models import Product, Promo


# Create your views here.
@login_required
def product_add(request):
    form = ProductAddForm()

    if request.method == 'POST':
        form = ProductAddForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()

            return redirect('index')

    context = {
        "form": form,
    }
    return render(request, 'product/product-add-page.html', context)


def product_detail(request, product_name):
    product = Product.objects.filter(slug=product_name).first()

    context = {
        "product": product,
    }

    return render(request, 'product/product-details-page.html', context=context)


@login_required
def product_edit(request, product_name):
    product = Product.objects.filter(slug=product_name).first()

    context = {
        "product": product,
    }

    return render(request, 'product/product-edit-page.html', context)


@login_required
def product_delete(request, product_name):
    product = Product.objects.filter(slug=product_name).first()

    context = {
        "product": product,
    }

    return render(request, 'product/product-delete-page.html', context)


@login_required
def add_products_to_promo(request):
    if request.method == 'POST':
        product_ids = request.POST.getlist('products')
        discount_percentage = Decimal(request.POST.get('discount_percentage'))
        promo_products = Product.objects.filter(pk__in=product_ids)

        for product in promo_products:
            promo = Promo(product=product, discount_percentage=discount_percentage)
            promo.calculate_discounted_price
            promo.save()

        return redirect('promo_products')  # Redirect to view all promo products
    else:
        products = Product.objects.all()
        return render(request, 'product/products_add_to_promo.html', {'products': products})


@login_required
def promo_products(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    promo_products = Promo.objects.all()

    context = {
        "all_products": products,
        "all_categories": categories,
        "promo_products": promo_products,
    }

    return render(request, 'product/promo_products.html', context)
