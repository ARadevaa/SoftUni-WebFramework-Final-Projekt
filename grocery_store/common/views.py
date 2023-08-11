from django.shortcuts import render
from grocery_store.common.forms import SearchForm
from grocery_store.product.models import Product, Promo


# Create your views here.
def index(request):
    products = Product.objects.all()
    promo_products = Promo.objects.all()

    search_form = SearchForm(request.GET)

    if search_form.is_valid():
        search_text = search_form.cleaned_data['search_text']
        products = products.filter(name__icontains=search_text)

    context = {
        "all_products": products,
        "search_form": search_form,
        "promo_products": promo_products,
    }

    return render(request, 'home-page.html', context=context)

