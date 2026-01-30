from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["nama_produk", "harga", "kategori", "status"]

    def clean_nama_produk(self):
        nama = self.cleaned_data["nama_produk"]
        if not nama:
            raise forms.ValidationError("Nama produk wajib diisi")
        return nama
