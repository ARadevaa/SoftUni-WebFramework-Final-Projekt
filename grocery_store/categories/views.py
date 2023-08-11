from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from grocery_store.categories.forms import CategoryCreateForm, SearchForm
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


# @group_required("Staff")
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


def category_list(request):
    categories = Category.objects.all()
    all_products = Product.objects.exclude(promo__isnull=False)
    promo_products = Promo.objects.all()
    paginator = Paginator(all_products, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    search_form = SearchForm(request.GET)

    if search_form.is_valid():
        search_text = search_form.cleaned_data['search_text']
        categories = categories.filter(name__icontains=search_text)

    context = {
        "all_products": all_products,
        "page_obj": page_obj,
        "all_categories": categories,
        "promo_products": promo_products,
        "search_form": search_form,
    }

    return render(request, 'category/category-details-page.html', context)


def category_edit(request):
    return render(request, 'category/category-edit-page.html')


def category_delete(request):
    return render(request, 'category/category-delete-page.html')
