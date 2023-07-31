from django.urls import path

from grocery_store.common.views import index

urlpatterns = (
    path('', index, name="index"),
)