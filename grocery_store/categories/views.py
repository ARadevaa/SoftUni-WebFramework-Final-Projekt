from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from grocery_store.cart.models import Cart
from grocery_store.categories.forms import CategoryCreateForm
from grocery_store.categories.models import Category
from grocery_store.product.models import Product, Promo


# Create your views here.

def products_by_category(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'products': products
    }

    return render(request, 'category/products_by_category.html', context)


def category_add(request):
    form = CategoryCreateForm

    if request.method == 'POST':
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()

            return redirect('index')

    context = {
        "form": form,
    }
    return render(request, 'category/category-add-page.html', context)

@login_required
def category_details(request):
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

    return render(request, 'category/category-details-page.html', context)


def category_edit(request):
    return render(request, 'category/category-edit-page.html')


def category_delete(request):
    return render(request, 'category/category-delete-page.html')
