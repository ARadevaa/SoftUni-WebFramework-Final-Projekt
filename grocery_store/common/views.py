from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from grocery_store.cart.models import Cart
from grocery_store.categories.models import Category
from grocery_store.common.forms import SearchForm
from grocery_store.product.models import Product, Promo


# Create your views here.
def index(request):
    # cart_items = Cart.objects.filter(user=request.user)
    # total_order_cost = sum(cart_item.total_price for cart_item in cart_items)
    products = Product.objects.all()
    promo_products = Promo.objects.all()

    search_form = SearchForm(request.GET)

    if search_form.is_valid():
        search_text = search_form.cleaned_data['search_text']
        products = products.filter(name__icontains=search_text)
        # promo_products = promo_products.product.filter(name__icontains=search_text) TODO: later

    # for product in products:
    #     product.liked_by_user = product.like_set \
    #         .filter(user=request.user) \
    #         .exists()

    context = {
        "all_products": products,
        # "comment_form": CommentForm(),
        "search_form": search_form,
        "promo_products": promo_products,
        # "cart_items": cart_items,
        # "total_order_cost": total_order_cost
    }

    return render(request, 'home-page.html', context=context)
