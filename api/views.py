from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer

# Create your views here.

def produk_list(request):
    produk = Product.objects.filter(status__nama_status="bisa dijual")
    return render(request, "api/produk_list.html", {"produk": produk})

def produk_add(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("produk_list")
    return render(request, "api/produk_form.html", {"form": form})

def produk_edit(request, id):
    produk = get_object_or_404(Product, id_produk=id)
    form = ProductForm(request.POST or None, instance=produk)
    if form.is_valid():
        form.save()
        return redirect("produk_list")
    return render(request, "api/produk_form.html", {"form": form})

def produk_delete(request, id):
    produk = get_object_or_404(Product, id_produk=id)
    produk.delete()
    return redirect("produk_list")

# ===== API VIEWS (JSON) =====

@api_view(["GET"])
def produk_api(request):
    produk = Product.objects.filter(status__nama_status="bisa dijual")
    serializer = ProductSerializer(produk, many=True)
    return Response(serializer.data)