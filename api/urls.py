from django.urls import path
from .views import produk_list, produk_add, produk_edit, produk_delete

urlpatterns = [
    path("produk/", produk_list, name="produk_list"),
    path("produk/add/", produk_add, name="produk_add"),
    path("produk/edit/<int:id>/", produk_edit, name="produk_edit"),
    path("produk/delete/<int:id>/", produk_delete, name="produk_delete"),
]
