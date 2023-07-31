from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from grocery_store.cart.models import Cart
from grocery_store.product.models import Product, Promo


# def add_to_bag(request, product_id):
#     # Get the product object
#     product = Product.objects.get(pk=product_id)
#
#     # Get the quantity added to the bag (assuming you have a quantity field in the bag model)
#     quantity_added_to_bag = request.POST.get('quantity')
#
#     # Reduce the product quantity in the storage
#     product.available_quantity -= int(quantity_added_to_bag)
#     product.save()
#
#     # Add the product to the user's bag (your existing logic to add to bag)
#
#     return redirect('success_url')  # Redirect to a success page or back to the product page

@login_required
def add_to_cart(request, product_name):
    product = get_object_or_404(Product, slug=product_name)

    if request.method == 'POST':
        quantity_added_to_bag = int(request.POST.get('quantity', 1))
        total_quantity = product.product_quantity * int(quantity_added_to_bag)

        if total_quantity <= 0:
            # Handle invalid quantity (e.g., less than or equal to 0)
            # You can add appropriate error handling or redirect to product detail page with a message
            return redirect('product details', slug=product_name)

        if product.available_quantity < total_quantity:
            # Handle insufficient stock
            # You can add appropriate error handling or redirect to product detail page with a message
            return redirect('product_detail', slug=product_name)

        cart_item, created = Cart.objects.get_or_create(
            user=request.user,
            product=product,
            defaults={'quantity': total_quantity}
        )

        if not created:
            product.available_quantity -= total_quantity
            product.save()
            cart_item.quantity += quantity_added_to_bag
            cart_item.save()

        return redirect('category details')
    else:
        return redirect('category details')


@login_required
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_order_cost = sum(cart_item.total_price for cart_item in cart_items)
    products = Product.objects.all()
    promo_products = Promo.objects.all()

    context = {
        "all_products": products,
        # "comment_form": CommentForm(),
        "promo_products": promo_products,
        "cart_items": cart_items,
        "total_order_cost": total_order_cost
    }

    return render(request, 'cart/view_cart.html', context)
