from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from decimal import Decimal
from django.urls import reverse_lazy
from django.views import generic as views
from grocery_store.categories.models import Category
from grocery_store.product.forms import ProductAddForm, ProductEditForm, ProductDeleteForm, SearchForm
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


class ProductDetailView(views.DetailView):
    model = Product
    template_name = 'product/product-details-page.html'
    context_object_name = 'product'
    slug_url_kwarg = 'product_name'
    slug_field = 'slug'


class ProductEditView(LoginRequiredMixin, views.UpdateView):
    model = Product
    form = ProductEditForm
    fields = '__all__'
    template_name = 'product/product-edit-page.html'
    context_object_name = 'product'
    slug_url_kwarg = 'product_name'
    slug_field = 'slug'


class ProductDeleteView(LoginRequiredMixin, views.DeleteView):
    form = ProductDeleteForm
    model = Product
    template_name = 'product/product-delete-page.html'
    success_url = reverse_lazy('inventory details')
    slug_url_kwarg = 'product_name'
    slug_field = 'slug'


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


def promo_products(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    promo_products = Promo.objects.all()
    search_form = SearchForm(request.GET)

    if search_form.is_valid():
        search_text = search_form.cleaned_data['search_text']
        promo_products = promo_products.filter(product__name__icontains=search_text)

    context = {
        "all_products": products,
        "all_categories": categories,
        "search_form": search_form,
        "promo_products": promo_products,
    }

    return render(request, 'product/promo_products.html', context)


class ProductListView(views.ListView):
    model = Product
    paginate_by = 10
    template_name = 'product/product_list.html'
    context_object_name = 'all_products'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.exclude(promo__isnull=False)
        search_query = self.request.GET.get('search_text')
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_form = SearchForm()
        context['search_form'] = search_form

        return context