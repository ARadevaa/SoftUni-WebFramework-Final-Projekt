from django.urls import path, include

from grocery_store.categories import views
from grocery_store.categories.views import category_add, category_list, category_edit, category_delete

urlpatterns = (
    path('add/', category_add, name="category add"),
    path('', category_list, name="category details"),
    path('<int:category_id>/', views.products_by_category, name='products_by_category'),
    # path(, include([
    #
    #     path('edit/', category_edit, name="category edit"),
    #     path('delete/', category_delete, name="category delete"),
    # ]))
)
